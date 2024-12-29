from flask import Blueprint, render_template

# template_folder를 지정한다(static은 지정하지 않는다)
dt = Blueprint("detector", __name__, template_folder="templates")


@dt.route("/")
def index():
    return render_template("detector/index.html")

