from app import app, db
from models import Restaurant, Pizza, RestaurantPizza
import random

with app.app_context():
    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    print("🍕 Seeding restaurants...")

    restaurants_data = [
        {"name": "New Pizza Place 1", "address": "123 Main St, Cityville"},
        {"name": "Awesome Pizzeria", "address": "456 Oak St, Townsville"},
        {"name": "Tasty Slices", "address": "789 Pine St, Villagetown"},
        {"name": "Pizza Junction", "address": "101 Elm St, Hamletville"},
        {"name": "Crunchy Crust", "address": "202 Maple St, Boroughburg"},
        {"name": "Pizza Oasis", "address": "303 Cedar St, Village Springs"},
        {"name": "Peppy Pies", "address": "404 Birch St, Orchard City"},
        {"name": "Dough Delight", "address": "505 Pine St, Town Haven"},
        {"name": "Tomato Temptations", "address": "606 Oak St, Groveburg"},
        {"name": "Pizzeria Paradiso", "address":"402 Waiyaki Way, Nairobi"}
    ]

    for data in restaurants_data:
        restaurant = Restaurant(**data)
        db.session.add(restaurant)

    db.session.commit()

    print("🍕 Seeding pizzas...")

    pizzas_data = [
        {"name": "Classic Margherita", "ingredients": "Tomato Sauce, Mozzarella, Basil"},
        {"name": "Spicy Pepperoni", "ingredients": "Tomato Sauce, Mozzarella, Pepperoni"},
        {"name": "Veggie Delight", "ingredients": "Tomato Sauce, Mozzarella, Bell Peppers, Mushrooms, Onions"},
        {"name": "Tropical Hawaiian", "ingredients": "Tomato Sauce, Mozzarella, Ham, Pineapple"},
        {"name": "BBQ Chicken Feast", "ingredients": "BBQ Sauce, Mozzarella, Grilled Chicken, Red Onion"},
    ]

    for data in pizzas_data:
        pizza = Pizza(**data)
        db.session.add(pizza)

    db.session.commit()

    print("🍕 Adding pizzas to restaurants...")

    prices = [10, 12, 14, 16, 24, 13, 5, 16, 3, 20]

    restaurants = Restaurant.query.all()
    pizzas = Pizza.query.all()

    for restaurant in restaurants:
        for _ in range(random.randint(1, 4)):
            pizza = random.choice(pizzas)
            price = random.choice(prices)

            restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza.id, restaurant_id=restaurant.id)
            db.session.add(restaurant_pizza)

    db.session.commit()

    print("🍕 Done seeding!")
