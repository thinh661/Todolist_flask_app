from flask import Flask
import os
from dotenv import load_dotenv
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta





load_dotenv()
SECRET_KEY = os.environ.get("SECRET_KEY")
DB_NAME = os.environ.get("DB_NAME")

sqlpass = 'Thinh123'
app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{sqlpass}@localhost/todolist'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

from .models import Note
from .models import User

from .user import user
from .views import views

    
app.register_blueprint(user)
app.register_blueprint(views)
    
login_manager = LoginManager()
login_manager.login_view = 'user.login'
login_manager.init_app(app=app)
app.permanent_session_lifetime = timedelta(minutes=1)

@login_manager.user_loader
def load_user(id) :
    return User.query.get(int(id))

