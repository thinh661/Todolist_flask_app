from flask import Blueprint,render_template,flash,request,jsonify
from flask_login import login_required,current_user
from .models import Note
from . import db
import json


views = Blueprint("views",__name__)

@views.route("/home",methods = ['POST','GET'])
@views.route('/',methods=['POST','GET'])
@login_required
def home():
    if request.method == 'POST' :
        note = request.form.get('note')
        if len(note) <1 :
            flash('Note kieu deo gi day?',"error")
        else:
            new_note = Note(data=note,user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Da them cong viec!",'success')
    return render_template("index.html",user = current_user)

@views.route('/delete-note',methods=['POST','GET']) 
def delete_note():
    note = json.loads(request.data)
    print(note)
    note_id = note['note_id']
    res = Note.query.get(note_id)
    if res :
        if res.user_id == current_user.id:
            db.session.delete(res)
            db.session.commit()
            flash("Da xoa node",'success')
    return jsonify({'code' : 200})