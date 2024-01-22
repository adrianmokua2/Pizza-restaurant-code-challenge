from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
    
    serialize_rules = ('-pizzas.restaurant',)  
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    
    pizzas = db.relationship('Pizza', secondary='restaurant_pizzas', back_populates='restaurants')

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'
    
    serialize_rules = ('-restaurant.restaurant_pizzas', '-pizza.restaurant_pizzas') 
    
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable= False)
    
    @validates('price')
    def checks_price(self, key, price):
        price_as_int = int(price) 
        if not (1 <= price <= 30):
            raise ValueError('must have a `price` between 1 and 30')
        else:
            return price    
        
class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'
    
    serialize_rules = ('-restaurants.pizzas',)  
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nullable=False)
    
    restaurants = db.relationship('Restaurant', secondary='restaurant_pizzas', back_populates='pizzas')

