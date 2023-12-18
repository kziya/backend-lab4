from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile('config.py', silent=True)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)

from src.auth import auth_controller
from src.category import category_controller
from src.user import user_controller
from src.record import record_controller
