from flask_login import UserMixin
from . import db 
from sqlalchemy.sql import func
from sqlalchemy import Column,Integer,String

class Note(db.Model) :
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True),default =func.now())
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"))
    
    def __init__(self,data,user_id):
        self.data = data
        self.user_id = user_id
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))
    user_name = db.Column(db.String(150))
    notes= db.relationship("Note")
    
    def __init__(self,email,password,user_name):
        self.email = email
        self.password = password
        self.user_name = user_name
    
    