from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Restaurant, Pizza, RestaurantPizza
import os

abs_path=os.getcwd()
db_path='sqlite:///'+abs_path+'/instance/app.db'

print(db_path)
app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)

# @app.route('/')
# def home():
#     return 'Restaurants'

class Index(Resource):
    def get(self):
        response_dict = {
            "message": "Nastro Pizzas Restaurant",
        }

        return make_response(jsonify(response_dict, 200))
    
api.add_resource(Index, '/')
    
class RestaurantsResource(Resource):
    def get(self):
        restaurants_query = Restaurant.query.all()
        restaurants = [{"id": restaurant.id, "name": restaurant.name, "address": restaurant.address} for restaurant in restaurants_query]
        return make_response(jsonify(restaurants), 200)

api.add_resource(RestaurantsResource, '/restaurants')

class RestaurantByIdResource(Resource):
    def get(self, restaurant_id):
        restaurant = Restaurant.query.get(restaurant_id)

        if restaurant:
            pizzas = [{"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients} for pizza in restaurant.pizzas]

            restaurant_data = {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address,
                "pizzas": [
                        {
                            "id": restaurant_pizza.pizza.id,
                            "name": restaurant_pizza.pizza.name,
                            "ingredients": restaurant_pizza.pizza.ingredients
                        }
                        for restaurant_pizza in restaurant.restaurant_pizzas
                    ]
            }

            return restaurant_data
        else:
            return {"error": "Restaurant not found"}, 404



    def delete(self, restaurant_id):
        restaurant = Restaurant.query.get(restaurant_id)
        
        if restaurant:
            RestaurantPizza.query.filter_by(restaurant_id=restaurant.id).delete()
            db.session.delete(restaurant)
            db.session.commit()
            
            return '', 204
        else:
            return {"error": "Restaurant not found"}, 404

api.add_resource(RestaurantByIdResource, '/restaurants/<int:restaurant_id>')

class PizzasResource(Resource):


    def get(self):
        pizzas = [{'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients} for pizza in Pizza.query.all()]
        return make_response(jsonify(pizzas), 200)


api.add_resource(PizzasResource, '/pizzas')

class RestaurantPizzasResource(Resource):
    def post(self):
        data = request.get_json()

        restaurant = Restaurant.query.filter(Restaurant.id == data['restaurant_id']).first()
        pizza = Pizza.query.filter(Pizza.id == data['pizza_id']).first()

        if not restaurant or not pizza:
            return {
                "errors": ["validation errors"]
            }, 404

        new_restaurant_pizza = RestaurantPizza(
            price=data['price'],
            restaurant_id=data['restaurant_id'],
            pizza_id=data['pizza_id']
        )

        db.session.add(new_restaurant_pizza)
        db.session.commit()

        pizza_data = {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        }

        return pizza_data, 201
    

api.add_resource(RestaurantPizzasResource, '/restaurant_pizzas')







if __name__ == '__main__':
    app.run(port=5555, debug=True)