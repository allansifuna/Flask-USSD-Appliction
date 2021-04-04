from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from somo.config import Config
from flask_redis import FlaskRedis
db = SQLAlchemy()
bcrypt = Bcrypt()
redis = FlaskRedis()
# lm = LoginManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    # app.url_map.default_subdomain = 'app'

    from somo.student.routes import student
    from somo.user.routes import user

    db.init_app(app)
    bcrypt.init_app(app)
    redis.init_app(app)
    # lm.init_app(app)

    app.register_blueprint(student)
    app.register_blueprint(user)

    return(app)
