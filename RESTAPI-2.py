
## Libraries
from flask import Flask, render_template, request, jsonify

## Creating Instance
app = Flask(__name__)

recipes = [{"ID":1, "NAME":"dosa", "DESCRIPTION":"masala dosa"},{"ID":2, "NAME":"rajma", "DESCRIPTION":"rajma chawal"}]

## task 1 : implement GET for /recipes --> return all recipes
@app.route('/recipes', methods=["GET"])
def home_get1():
    if request.method == "GET":
        json_data = jsonify(recipes)

        return json_data


## task 2 : implement GET for /recipes.id --> return the recipe whose id matches with id passed
@app.route('/recipes/<int:ID>', methods=["GET"])
def home_get2(ID):

    if request.method == "GET":

        json_data = jsonify(recipes)

        for i in recipes:
            if i['ID'] == ID:
                return i
        else:
            return("Value Error")


## task 3:
@app.route('/recipes/<int:ID>', methods=["DELETE"])
def home_delete(ID):
    if request.method == "DELETE":
        for i in recipes:
            if i['ID'] == ID:
                recipes.remove(i)
                return recipes
        else:
            return("Value Error")



## task 4:
@app.route('/recipes/<int:ID>', methods=["PUT"])
def home_update(ID):
    if request.method == "PUT":
        for i in recipes:
            if i['ID'] == ID:
                data = request.get_json()
                i.update(data)
                return recipes
        else:
            return("Value Error")

## task 5: implement post for recipes --> to add new recipes
@app.route('/recipes', methods=["POST"])
def home_post():
    if request.method == "POST":
        data = request.get_json()
        recipes.append(data)

        return recipes
    


app.run()