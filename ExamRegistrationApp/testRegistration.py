## Libraries
from flask import Flask, render_template, request, jsonify
import requests
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from http import HTTPStatus
from passlib.hash import pbkdf2_sha256
from flask_migrate import Migrate

## Creating instance
app = Flask(__name__)

## setting up configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/exam_registration'
api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

## Fetching data from database
class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    # email = db.Column(db.String(200), nullable=False)

    @staticmethod
    def add_exam(name, password):
        password = pbkdf2_sha256.hash(password)
        new_exam = Exam(name=name, password=password)
        db.session.add(new_exam)
        db.session.commit()


    @staticmethod
    def get_all_candidates():
        return Exam.query.all()


    @staticmethod
    def check_if_user_exist(name):
        data = Exam.query.all()

        for i in data:
            if i.name == name:
                return True
        else:
            return False

    @staticmethod
    def check_if_password_matches(password):
        data = Exam.query.all()

        for i in data:
            if pbkdf2_sha256.verify(i.password,password):
                return True
        else:
            return False


## Interacting with webpage via html and pycharm
# Entry Page
@app.route('/')
def entry_page():
    return render_template("ExamHome.html")

# print("checking function validity: ",Exam.check_if_user_exist(name="Tony Stark"))

@app.route('/signup', methods = ["GET","POST"])
def sign_up_page():
    if request.method == "GET":
        return render_template("signUser.html")

    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]

        user_status = Exam.check_if_user_exist(name)  # It will give status True or False
        print(user_status)

        if user_status:
            return render_template("signUser.html",exist = True)
        else:
            Exam.add_exam(name=name, password=pbkdf2_sha256.hash(password))
            return render_template("signUser.html", exist=False)
    # else:
    #     return render_template("signUser.html", exist = False)



@app.route('/login', methods = ["GET","POST"])
def login_page():
    if request.method == "GET":
        return render_template("loginUser.html")

    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]

        user_status = Exam.check_if_user_exist(name)

        if user_status:
            return content_page()
        else:
            return render_template("loginUser.html",exist= False)


@app.route('/content', methods = ["GET","POST"])
def content_page():
    if request.method == "POST":
        return render_template("content.html")


## Running the application
if __name__ == "__main__":
        app.run()





