
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from http import HTTPStatus

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/MovieDatabase'

api = Api(app)

db = SQLAlchemy(app)

# class Profile(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    title = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(80), nullable=False)

    @staticmethod
    def add_movie(title, year, genre):
        new_movie = Movie(title=title, year=year, genre=genre)
        db.session.add(new_movie)
        db.session.commit()


    @staticmethod
    def get_one_movie(id):
        my_movie = Movie.query.filter_by(id = id).first()
        return my_movie


    @staticmethod
    def delete_movie(id):
        my_movie = Movie.query.filter_by(id=id).delete()
        return my_movie

    # @staticmethod
    # def put_movie(id):
    #     my_movie = Movie.query.filter_by(id=id).add()
    #     return my_movie


    @staticmethod
    def get_movie():
        return Movie.query.all()


    @staticmethod
    def update_movie(id):
        updated_data = Movie.query.filter_by(id=id).update(request.get_json())
        db.session.commit()
        return updated_data



class all_movies(Resource):
    def post(self):
        data = request.get_json()
        print(data)
        Movie.add_movie(title=data["title"], year=data["year"], genre=data["genre"])
        return {"status": HTTPStatus.OK}


    def get(self):
        data = Movie.get_movie()
        movieLst = []

        for i in data:
            temp_dict = {'title':i.title, 'year':i.year, 'genre':i.genre}
            movieLst.append(temp_dict)
        return jsonify((movieLst), {"status": HTTPStatus.OK})


# class one_movie(Resource):
#     def get(self,id):
#         data = Movie.get_movie()
#         movieLst = []
#         for i in data:
#             if i.id == id:
#                 temp_dict = {'title': i.title, 'year': i.year, 'genre': i.genre}
#                 movieLst.append(temp_dict)
#                 return movieLst
#         else:
#             return {"message":"ID not found", "status":HTTPStatus.NOT_FOUND}

class one_movie(Resource):
    def get(self,id):
        data = Movie.get_one_movie(id)
        print(data)
        if data:
            movieDict = {"title":data.title, "year":data.year, "genre":data.genre}
            return jsonify((movieDict), {"status": HTTPStatus.OK})
        else:
            return {"message":"ID not found", "status":HTTPStatus.NOT_FOUND}


    def delete(self,id):
        # data = Movie.get_movie()
        # print(data)
        data= Movie.delete_movie(id)
        if data:
            return HTTPStatus.OK
        else:
            return HTTPStatus.NOT_FOUND


    def put(self,id):
        new_data = Movie.update_movie(id)
        print(new_data)
        data = Movie.get_movie()
        print(data)
        if data:
            movieLst = []
            for mo in data:
                movieLst.append({"title":mo.title, "year":mo.year, "genre":mo.genre})
            return jsonify((movieLst), {"status": HTTPStatus.OK})
        else:
            return {"message": "ID not found", "status": HTTPStatus.NOT_FOUND}




# def delete(self,id):
    #     data = Movie.get_movie()
    #     print(data)
    #     for mo in data:
    #         print(mo.id)
    #         if mo.id == id:
    #             Movie.delete_movie(id)
    #             db.session.commit()
    #             return HTTPStatus.OK
    #     else:
    #         return HTTPStatus.NOT_FOUND


    # def put(self, id):







api.add_resource(all_movies, "/movies")
api.add_resource(one_movie, "/movies/<int:id>")

app.run()


## Commands in terminal to enter to interact with db via pycharm
# 1) from flask_sqlalchemy_1 import db
# 2) db.create_all()
# 3) from flask_sqlalchemy_1 import Profile
# 4) tryadmin1 = Profile(username = "new user", email = "email@xyz.com")
# 5) db.session.add(tryadmin1)
# 6) db.session.commit()
# 7) Movie.query.all()
# 8) Movie.query.filter_by(username = 'Profile 1').first()







