#!/usr/bin/env python3

from flask import Flask, jsonify, make_response, Response, json, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from collections import OrderedDict


from models import Restaurant, RestaurantPizza, Pizza, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

class Index(Resource):
    
    def get(self):
         
         response_dict={
             "message":"Welcome to Restaurant domain API"
         }
        
         return make_response(
             jsonify(response_dict),
             200
         )
    
api.add_resource(Index, '/')

class Restaurants(Resource):
    def get(self):
        restaurants = Restaurant.query.all()
          
        restaurant_dict = [
                   OrderedDict([
                   ('id', restaurant.id),
                   ('name', restaurant.name),
                   ('address', restaurant.address)
                    ]) for restaurant in restaurants
                    ]

        response_json = json.dumps(restaurant_dict, sort_keys=False, indent=2)

        return Response(response_json, content_type='application/json; charset=utf-8', status=200)

api.add_resource(Restaurants, '/restaurants')

class RestaurantByID(Resource):
    def get(self, id):
        restaurant= Restaurant.query.filter_by(id=id).first()
        
        if restaurant is None:
            return make_response(
               jsonify({"error": "Restaurant not found"}), 
               404
            )
            
        else:
          pizzas_dict = [
            OrderedDict([
                ('id', pizza.id),
                ('name', pizza.name),
                ('ingredients', pizza.ingredients)    
        ]
        ) for pizza in restaurant.pizzas
        ]
        
        response_data = OrderedDict([
            ('id', restaurant.id),
            ('name', restaurant.name),
            ('address', restaurant.address),
            ('pizzas', pizzas_dict)
        ]    
        )
        
        
        response_json = json.dumps(response_data, sort_keys=False, indent=2)

        return Response(response_json, content_type='application/json; charset=utf-8', status=200)
    def delete(self,id):
        
        restaurant = Restaurant.query.filter_by(id=id).first()

        if restaurant:
            RestaurantPizza.query.filter_by(restaurant_id=id).delete()
            
            try:
                db.session.delete(restaurant)
                db.session.commit()
                
            except Exception as e:
                db.session.rollback()
                return {'error': str(e)}, 500
            
            response = make_response(jsonify(""), 204)
            return response
        
        else:
            response = make_response(jsonify({ "error": "Restaurant not found"}), 404)
            return response

          
       
api.add_resource(RestaurantByID, '/restaurants/<int:id>')

class Pizzas(Resource):
    def get(self):
        
        pizzas = Pizza.query.all()
        
        response_data = [
            OrderedDict([
            ('id', pizza.id),
            ('name', pizza.name),
            ('ingredients', pizza.ingredients),
            ] 
            ) for pizza in pizzas
        ]
        response_json = json.dumps(response_data, sort_keys=False, indent=2)

        return Response(response_json, content_type='application/json; charset=utf-8', status=200)

api.add_resource(Pizzas, '/pizzas')
        
class RestaurantPizzas(Resource):
    def post(self):
        
        restaurant_pizza = RestaurantPizza(
            
            price= request.form.get('price'),
            pizza_id=request.form.get('pizza_id'),
            restaurant_id =request.form.get('restaurant_id'),
        
        )
        
        db.session.add(restaurant_pizza)
        db.session.commit()
        
        if restaurant_pizza:
            pizza = Pizza.query.get(restaurant_pizza.pizza_id)

            
            response_data = OrderedDict([
                       ('id', pizza.id),
                       ('name', pizza.name),
                       ('ingredients', pizza.ingredients),
                     ] 
                     )  
                     
            
            response_json = json.dumps(response_data, sort_keys=False, indent=2)

            return Response(response_json, content_type='application/json; charset=utf-8', status=200)
            
            
        else:
            response = {"errors": ["validation errors"] }
            return make_response(
                jsonify(response), 
                404
                )
        
api.add_resource(RestaurantPizzas,'/restaurant_pizzas')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
    


