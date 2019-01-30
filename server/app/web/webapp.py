import os
from flask import Blueprint, render_template, send_from_directory, current_app, request


bp = Blueprint("webapp", __name__, template_folder="templates")


@bp.route("/")
def index():
    url_base = request.base_url + "api/"
    dataset_title = current_app.config["DATASET_TITLE"]
    return render_template("index.html", prefix=url_base, datasetTitle=dataset_title)


# renders swagger documentation
@bp.route("/swagger")
def swag():
    prefix = request.base_url
    prefix = prefix[:prefix.rfind("/swagger")]
    return render_template("swagger.html", prefix=prefix)


# renders swagger documentation
@bp.route("/favicon.png")
def favicon():
    return send_from_directory(os.path.join(bp.root_path, "static/img/"), "favicon.png")
