import os
from flask import Flask, render_template, url_for, session, request, redirect
from models import *
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///school.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return redirect(url_for('login'))

@app.route("/student")
def student():
    tid = session.get("uid")
    lec = lecture.query.filter_by(teacher_id=tid).all()
    x = lecture.query.all()
    return render_template("follow.html", lectures=x)

@app.route("/teacher")
def teacher_dashboard():
    return "Teacher Dashboard"

@app.route("/admin")
def admin():
    return "Admin Dashboard"

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_name = request.form.get('name')
        password = request.form.get('password')

        loged = user.query.filter_by(name=user_name, password=password).first()
        if loged:
            session["user_name"] = user_name
            session["password"] = password
            session["uid"] = loged.id
            session["type"] = "s"
            return redirect(url_for('student'))

        loged = teacher.query.filter_by(name=user_name, password=password).first()
        if loged:
            session["user_name"] = user_name
            session["password"] = password
            session["uid"] = loged.id
            session["type"] = "t"
            return redirect(url_for('teacher_dashboard'))

        loged = admin.query.filter_by(name=user_name, password=password).first()
        if loged:
            session["user_name"] = user_name
            session["password"] = password
            session["uid"] = loged.id
            session["type"] = "a"
            return redirect(url_for('admin'))

        return render_template("login.html", error="Invalid credentials.")
    else:
        return render_template("login.html")

@app.route("/register")
def choose_register_type():
    return render_template("choose_register.html")

@app.route("/register/<string:x>", methods=["GET", "POST"])
def register(x):
    if request.method == "POST":
        user_name = request.form.get('name')
        password = request.form.get('password')
        email = request.form.get('email')
        phone = request.form.get('phone')
        age = request.form.get('age')

        if x == "Student":
            tid = request.form.get('tid')
            new_user = user(name=user_name, password=password, email=email, phone=phone, age=age, tid=tid)
            db.session.add(new_user)
        elif x == "Teacher":
            new_teacher = teacher(name=user_name, password=password, email=email, phone=phone, age=age)
            db.session.add(new_teacher)
        elif x == "Admin":
            new_admin = admin(name=user_name, password=password, email=email, phone=phone, age=age)
            db.session.add(new_admin)
        db.session.commit()
        return redirect(url_for('login'))
    else:
        return render_template("register.html", x=x)

if __name__ == "__main__":
    app.run(debug=True)
