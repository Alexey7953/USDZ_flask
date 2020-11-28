from flask import Flask


from blueprints.auth import bp as auth_bp

from database.database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('src.config.Config')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    db.init_app(app)
    return app
