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

if __name__ == '__main__':
    app.run(port=5555, debug=True)