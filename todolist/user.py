from flask import Blueprint,render_template,request,flash,redirect, session,url_for
from .models import User,Note
from werkzeug.security import generate_password_hash
from . import db
from flask_login import login_user,login_required,logout_user,current_user


user = Blueprint("user",__name__)

@user.route("/login", methods= ['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if password == user.password :
                session.permanent = True    
                login_user(user=user,remember=True)
                flash("login thanh cong",'success')
                return redirect(url_for('views.home'))
                # return "Ban da login thanh cong, dang ra ban se duoc vao trang home"
            else :
                flash("Mat khau hoac email sai",'error')
                return redirect(url_for('user.login'))
        else :
            flash("User khong ton tai!","error")
            return redirect(url_for('user.login'))
    return render_template("login.html",user= current_user)

@user.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.login'))

@user.route("/signup",methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        user_name = request.form.get('user_name')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        user = User.query.filter_by(email = email).first()
        if user:
            flash("User da ton tai","error")
        elif len(email) > 150 :
            flash("email qua dai",'error')
        elif len(password) <7 :
            flash("pass qua ngan",'error')
        elif password != confirm_password :
            flash('pass và confirm password k giong nhau','error')
        else :
            # password = generate_password_hash(password=password,method='sha256')
            new_user = User(email=email,password=password,user_name=user_name)
            try :
                db.session.add(new_user)
                db.session.commit()
                login_user(user=new_user,remember=True)
                flash("Da tao tai khoan",'success')
                return redirect(url_for('views.home'))
            except:
                "error"
    return render_template('signup.html',user=current_user)