#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request, Response
from flask_migrate import Migrate

from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return f'<h1>Hello, Welcome to the Pizza Restaurant App!</h1>'

@app.route("/restaurants", methods=['GET'])
def get_restaurants():
    restaurants = [restaurant.to_dict() for restaurant in Restaurant.query.all()]
    response = make_response(jsonify(restaurants), 200)
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route("/restaurants/<int:restaurant_id>", methods=["GET"])
def get_restaurant_by_id(restaurant_id):
    restaurant = Restaurant.query.filter_by(id=restaurant_id).first()
    if not restaurant:
        response_body = {"error": "Restaurant not found"}
        response = make_response(jsonify(response_body), 404)
        return response

    else:
        if request.method == "GET":
            restaurant_dict = restaurant.to_dict()

            response = make_response(
                jsonify(restaurant_dict),
                200,
            )
            response.headers["Content-Type"] = "application/json"

            return response
        
@app.route("/restaurants/<int:restaurant_id>", methods=["DELETE"])
def delete_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)

    if not restaurant:
        response_body = {"error": "Restaurant not found"}
        response = make_response(jsonify(response_body), 404)
        return response

    RestaurantPizza.query.filter_by(restaurant_id=restaurant_id).delete()

    db.session.delete(restaurant)
    db.session.commit()

    response = make_response("", 204) 
    return response

@app.route("/pizzas", methods=["GET"])
def get_pizzas():
    if request.method == "GET":
        pizzas = [pizza.to_dict() for pizza in Pizza.query.all()]
        response = make_response(
            jsonify(pizzas),
            200,
        )
        response.headers["Content-Type"] = "application/json"

        return response


@app.route("/restaurant_pizzas", methods=["POST"])
def create_restaurant_pizza():
    try:

        data = request.get_json()

        required_fields = ["price", "pizza_id", "restaurant_id"]
        if not all(field in data for field in required_fields):
            raise ValueError("Validation errors: Missing required fields")

        price = data["price"]
        pizza_id = data["pizza_id"]
        restaurant_id = data["restaurant_id"]

        if not 1 <= price <= 30:
            raise ValueError("Validation errors: Price must be between $1 and $30")

        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)

        if not pizza or not restaurant:
            raise ValueError("Validation errors: Invalid Pizza ID or Restaurant ID")

        new_restaurant_pizza = RestaurantPizza(price=price, restaurant_id=restaurant_id, pizza_id=pizza_id,)

        db.session.add(new_restaurant_pizza)
        db.session.commit()

        pizza_data = {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients,
        }

        response = make_response(jsonify(pizza_data), 201) 
        response.headers["Content-Type"] = "application/json"
        return response

    except ValueError as e:
    
        response_body = {"errors": [str(e)]}
        response = make_response(jsonify(response_body), 400)
        return response


if __name__ == '__main__':
    app.run(port=5555, debug=True)