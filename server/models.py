from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
    serializer_rules = ('-restaurant.pizzas',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    address = db.Column(db.String, unique=True, nullable=False)

    pizzas = db.relationship('Pizza', secondary='restaurantpizza', backref='restaurant')
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "pizzas": [{"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients} for pizza in self.pizzas],
        }

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'
    serializer_rules = ('-pizza.restaurants',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    restaurants = db.relationship('Restaurant', secondary='restaurantpizza', backref='pizza')

    @validates('price')
    def validate_price(self, key, price):
        if not 1 <= price <= 30:
            raise ValueError("Price must be between $1 and $30.")
        return price

   
class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurantpizza'
    serializer_rules = ('-restaurant.pizzas', '-pizza.restaurants')

    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    

    
    