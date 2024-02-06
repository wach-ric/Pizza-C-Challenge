from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

db = SQLAlchemy()

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    pizzas = db.relationship('RestaurantPizza', back_populates='restaurant')

   
    @validates('name')
    def validate_name_length(self, key, name):
        if len(name) > 45:
            raise ValueError("Name must be less than or equal to 45 characters")
        return name
    
    def __repr__(self):
        return f'<Restaurant {self.name}>'
    

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    ingredients = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='pizza')

    
    def __repr__(self):
        return f'<Pizza {self.name}>'
    
class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    name = db.Column(db.String(255))  
    ingredients = db.Column(db.String(255))
    price = db.Column(db.Integer, nullable=False) 
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    restaurant = db.relationship('Restaurant', back_populates='pizzas')
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')
     
    @validates('price')
    def validate_price(self, key, price):
        price_range = range(1, 31)  
        if price not in price_range:
            raise ValueError("Price must be within the range of 1 to 30")
        return price
    
    def __repr__(self):
        return f'<RestaurantPizzas {self.price}>'