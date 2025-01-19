# from pathlib import Path  # 경로작업

from flask import Flask

# flask-login LoginManager를 import
from flask_login import LoginManager  # type: ignore

# 마이그레이션 작업을 위해
from flask_migrate import Migrate  # type: ignore

# SQL작업을 위해
from flask_sqlalchemy import SQLAlchemy

# flask-wtf 모듈의 CSRFProtect import
from flask_wtf.csrf import CSRFProtect  # type: ignore

# config 모듈을 import
from apps.config import config

# SQLAlchemy를 인스턴스화 한다.
db = SQLAlchemy()

# CSRFProtect 객체 생성
csrf = CSRFProtect()


# LoginManager 객체 생성
login_manager = LoginManager()
# login_view 속성에 미 로그인시 리다이렉트하는 엔드포인트를 지정
login_manager.login_view = "auth.login"
# login_massage 속성 : 로그인시 표시할 메세지를 지정. 현재는 표시할 내용없어서 "공백"
# login_massage는 기본값으로 설정되어 있어요. 영어로 값이 이미 존재함 그래서 그 메세지를 지우기위해!
login_manager.login_message = ""


# create_app 함수를 작성한다.
def create_app(local):
    # Flask 인스턴스 생성
    app = Flask(__name__)
    # app의 config 설정을 한다
    app.config.from_object(config[local])
    # app.config.from_envvar("APPLICATION_SETTINGS")
    # app.config.from_pyfile("envconfig.py")
    # app.config.from_mapping(
    #     SECRET_KEY="DM5Fq1G9XtMzWAeqYWNR",
    #     SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
    #     # __file__ : 현재파일인 경로를 알려준다.
    #     SQLALCHEMY_TRACK_MODIFICATIONS=False,
    #     # SQL 콘솔 로그에 출력
    #     SQLALCHEMY_ECHO=True,
    #     WTF_CSRF_SECRET_KEY="El1oD921KMdGKONsydDa",
    #     # CSRF 공격 방지를 위한 토큰 생성 키값.
    # )

    # SQLAlchemy와 앱을 연계한다
    db.init_app(app)
    # Migrate와 앱을 연계한다
    Migrate(app, db)

    # login_manager를 app과 연계
    login_manager.init_app(app)

    # crud 패키지로부터 views를 import한다.
    # views.py 모듈은 @app.route()와 같은 맵핑 기능을 가진 모듈
    from apps.crud import views as crud_views  # as 이후 별칭 선언

    # app.register_blueprint를 사용해 views의 crud를 앱에 등록한다.
    # 엔드포인트 앞에 crud가 붙게 됨.
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    # AUTH 패키지로 부터 views 모듈을 import
    from apps.auth import views as auth_views

    # register_blueprint()로 blueprint 등록
    app.register_blueprint(auth_views.auth, url_prefix="/auth")

    # 이제부터 작성하는 detector 패키지로부터 views를 import한다
    from apps.detector import views as dt_views
    
    # register_blueprint를 사용해 views의 dt를 앱에 등록한다
    app.register_blueprint(dt_views.dt)

    return app
