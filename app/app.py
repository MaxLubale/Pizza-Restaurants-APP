#!/usr/bin/env python3

from flask import Flask, request, jsonify
from models import db, Restaurant, Pizza, RestaurantPizza
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurant.db'
db.init_app(app)
migrate = Migrate(app, db)

# Routes

@app.route('/')
def home():
    return '<h1>Welcome to the restaurants pizzas API</h1>'

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    try:
        restaurants = Restaurant.query.all()
        data = [{'id': restaurant.id, 'name': restaurant.name, 'address': restaurant.address} for restaurant in restaurants]
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    try:
        restaurant = Restaurant.query.get(id)
        if restaurant:
            data = {
                'id': restaurant.id,
                'name': restaurant.name,
                'address': restaurant.address,
                'pizzas': [{'id': p.id, 'name': p.name, 'ingredients': p.ingredients} for p in restaurant.pizzas]
            }
            return jsonify(data)
        else:
            return jsonify({'error': 'Restaurant not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    try:
        restaurant = Restaurant.query.get(id)
        if restaurant:
            # Delete associated RestaurantPizzas
            RestaurantPizza.query.filter_by(restaurant_id=id).delete()
            # Delete the restaurant
            db.session.delete(restaurant)
            db.session.commit()
            return '', 204
        else:
            return jsonify({'error': 'Restaurant not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    try:
        pizzas = Pizza.query.all()
        pizza_list = [{'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients} for pizza in pizzas]
        return jsonify(pizza_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    try:
        data = request.json
        required_fields = ['price', 'pizza_id', 'restaurant_id']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400

        restaurant_pizza = RestaurantPizza(price=data['price'], pizza_id=data['pizza_id'], restaurant_id=data['restaurant_id'])
        db.session.add(restaurant_pizza)
        db.session.commit()
        pizza = Pizza.query.get(data['pizza_id'])
        return jsonify({'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(port=3000, debug=True)
