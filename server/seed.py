# from app import app, db
# from faker import Faker
# import random
# from models import Restaurant, Pizza, RestaurantPizza

# fake = Faker()

# def seed():
#     # Create and add fake restaurants
#     for _ in range(5):  # Adjust the number of restaurants as needed
#         restaurant = Restaurant(
#             name=fake.company(),
#             address=fake.address(),
#         )
#         db.session.add(restaurant)

#     db.session.commit()

#     # Create and add fake pizzas
#     for _ in range(10):  # Adjust the number of pizzas as needed
#     # Generate a unique name
#         unique_name = fake.word()
#         while Pizza.query.filter_by(name=unique_name).first() is not None:
#             unique_name = fake.word()

#         pizza = Pizza(
#             name=unique_name,
#             ingredients=','.join(fake.words(3)),  # Join ingredients into a comma-separated string
#             price=random.randint(5, 25),
#         )
#         db.session.add(pizza)

#     db.session.commit()

#     # Associate fake pizzas with fake restaurants using the RestaurantPizza association table
#     restaurants = Restaurant.query.all()
#     pizzas = Pizza.query.all()

#     for restaurant in restaurants:
#         pizzas_for_restaurant = random.sample(pizzas, random.randint(1, 3))
#         for pizza in pizzas_for_restaurant:
#             restaurant_pizza = RestaurantPizza(restaurant_id=restaurant.id, pizza_id=pizza.id)
#             db.session.add(restaurant_pizza)


#     db.session.commit()

#     print("Database seeded successfully!")

# if __name__ == '__main__':
#     with app.app_context():
#         seed()

from app import app, db
from faker import Faker
import random
from models import Restaurant, Pizza, RestaurantPizza

fake = Faker()

# Predefined lists of pizza names and ingredients for a more realistic seeding
pizza_names = ['Margherita', 'Pepperoni', 'Quattro Formaggi', 'Hawaiian', 'Vegetarian', 'Meat Lovers', 'Mushroom Lovers', 'BBQ Chicken', 'Capricciosa', 'Supreme']
pizza_ingredients = ['Cheese', 'Tomatoes', 'Pepperoni', 'Mushrooms', 'Onions', 'Bell Peppers', 'Olives', 'Ham', 'Pineapple', 'Bacon', 'Chicken', 'BBQ Sauce']

def seed():

    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()
    
    # Create and add fake restaurants
    for _ in range(5):
        restaurant = Restaurant(
            name=fake.company(),
            address=fake.address(),
        )
        db.session.add(restaurant)

    db.session.commit()

    # Create and add fake pizzas with realistic names and ingredients
    for _ in range(10):
        pizza_name = random.choice(pizza_names)
        pizza_ingredient_list = random.sample(pizza_ingredients, random.randint(2, 5))
        pizza = Pizza(
            name=pizza_name,
            ingredients=','.join(pizza_ingredient_list),
            price=random.randint(5, 25),
        )
        db.session.add(pizza)

    db.session.commit()

    # Associate fake pizzas with fake restaurants using the RestaurantPizza association table
    restaurants = Restaurant.query.all()
    pizzas = Pizza.query.all()

    for restaurant in restaurants:
        pizzas_for_restaurant = random.sample(pizzas, random.randint(1, 3))
        for pizza in pizzas_for_restaurant:
            restaurant_pizza = RestaurantPizza(restaurant_id=restaurant.id, pizza_id=pizza.id)
            db.session.add(restaurant_pizza)

    db.session.commit()

    print("Database seeded successfully!")

if __name__ == '__main__':
    with app.app_context():
        seed()
