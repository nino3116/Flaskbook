import uuid  # uuid를 import한다.
from pathlib import Path  # Path를 import한다
from apps.app import db
from apps.crud.models import User
from apps.detector.models import UserImage
from apps.detector.forms import UploadImageForm
from flask import (Blueprint,
                   render_template,
                   current_app,
                   send_from_directory,
                   redirect,
                   url_for,
)
# login_required, cuurent_user를 import한다
from flask_login import current_user, login_required

# template_folder를 지정한다(static은 지정하지 않는다)
dt = Blueprint("detector", __name__, template_folder="templates")


@dt.route("/")
def index():
    #User와 UserImage를 Join해서 이미지 알람을 취득한다.
    user_images = (
        db.session.query(User, UserImage)
        .join(UserImage)
        .filter(User.id == UserImage.user_id)
        .all()
    )
    return render_template("detector/index.html", user_images=user_images)


@dt.route("/images/<path:filename>")
def image_file(filename):
    return send_from_directory(current_app.config['UPLOAE_FOLDER'], filename)
            # 템플릿으로 표시하려면 다음과 같이 기술하세요.
            # url_for ('detector.image_file', filename='이미지 파일명')
            
            
@dt.route("/upload", methods=["GET", "POST"])
# 로그인을 필수로 하기
@login_required
def upload_image():
    # UploadImageForm을 이용해서 검증한다
    form = UploadImageForm()
    if form.validate_on_submit():
        # 업로드된 이미지 파일을 취득하기
        file = form.image.data
        # 파일의 파일명과 확장자를 취득하고, 파일명을 uuid로 변환한다.
        ext = Path(file.filename).suffix
        image_uuid_file_name = str(uuid.uuid4()) + ext # 랜덤값으로 파일명을 uuid로 변환
        # 이미지를 저장한다
        image_path = Path(
            current_app.config["UPLOAD_FOLDER"], image_uuid_file_name
        )
        file.save(image_path)
        
        # DB에 저장한다
        user_image = UserImage(
            user_id = current_user.id, image_path = image_uuid_file_name
        )
        db.session.add(user_image)
        db.session.commit()
        
        return redirect(url_for("detector.index"))
    return render_template("detector/upload.html", form=form)