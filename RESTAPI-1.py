## Libraries
from flask import Flask, render_template, request, jsonify

## Creating Instance
app = Flask(__name__)

user_list = [{"name":"sachin","age":40}]

## Home Page
@app.route('/', methods=["GET"])
def home_get():
    if request.method == "GET":
        json_data = jsonify(user_list)

        return json_data


@app.route('/', methods=["POST"])
def home_post():
    if request.method == "POST":
        data = request.get_json()
        user_list.append(data)

        return user_list


@app.route('/', methods=["DELETE"])
def home_delete():
    if request.method == "DELETE":
        user_list.clear()
        return user_list


@app.route('/<int:age>', methods=["PUT"])
def home_update(age):
    print(age)
    if request.method == "PUT":
        for i in user_list:
            if i['age'] == 35:
                i.update({'name':'dhoni', 'age':age})

    return user_list


app.run()


