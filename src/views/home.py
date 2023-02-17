
from flask import Blueprint, render_template

bp = Blueprint('index', __name__, url_prefix='/home')


@bp.route('/')
def base():
    return render_template("base.html")