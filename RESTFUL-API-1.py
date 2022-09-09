## Libraries
from flask import Flask, request, jsonify
from flask_restful import Api, Resource

## Creating Instance
app = Flask(__name__)
api = Api(app)

recipes = [{"ID":1, "NAME":"dosa", "DESCRIPTION":"masala dosa"},{"ID":2, "NAME":"rajma", "DESCRIPTION":"choley bhature"}]

## Creating Classes

# 1) methods that will pass entire list
class allRecipes(Resource):
    def get(self):
        json_data = jsonify(recipes)
        return json_data

    def post(self):
        data = request.get_json()
        print(type(data))
        recipes.append(data)
        return jsonify(recipes)


class oneRecipes(Resource):
    def get(self,ID):
        for i in recipes:
            if i['ID'] == ID:
                return jsonify(i)
        else:
            return jsonify({"message":"Value Error"})


    def put(self, ID):
        for i in recipes:
            if i['ID'] == ID:
                data = request.get_json()
                i.update(data)
                return jsonify(recipes)
        else:
            return jsonify({"message":"Value Error"})


    def delete(self, ID):
        for i in recipes:
            if i['ID'] == ID:
                recipes.remove(i)
                return jsonify(recipes)
        else:
            return jsonify({"message":"Value Error"})


api.add_resource(allRecipes,"/recipes")
api.add_resource(oneRecipes,"/recipes/<int:ID>")
app.run()

