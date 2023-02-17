import os
import uuid
from flask import Flask,redirect
from .config import DefaultConfig


def create_app():
    app = Flask(__name__, instance_relative_config=True,template_folder='templates')
    configure_app(app)
    configure_views(app)
    return app

def configure_views(app):
    
    from src.views import DEFAULT_VIEWS as views
    for view in views:
        app.register_blueprint(view)

    @app.route('/')
    def root_path():
        return redirect("/home", code=302)


def configure_app(app):
    app.config.from_object(DefaultConfig)