from app import db, Restaurant, Pizza, RestaurantPizza

def seed_data():
    # Create sample data
    restaurant1 = Restaurant(name='Sottocasa NYC', address='298 Atlantic Ave, Brooklyn, NY 11201')
    restaurant2 = Restaurant(name='PizzArte', address='69 W 55th St, New York, NY 10019')
    restaurant3 = Restaurant(name='Slice House', address='123 Main St, Anytown, USA')
    restaurant4 = Restaurant(name='Pizza Palace', address='456 Oak St, Cityville, USA')
    restaurant5 = Restaurant(name='Mamma Mia Pizzeria', address='789 Elm St, Villagetown, USA')
    restaurant6 = Restaurant(name='Crust & Crumble', address='101 Pine St, Riverside, USA')
    restaurant7 = Restaurant(name='The Oven', address='202 Maple Ave, Hillside, USA')
    restaurant8 = Restaurant(name='Top Toppings', address='303 Cedar St, Lakeside, USA')
    restaurant9 = Restaurant(name='Artisan Pies', address='404 Birch St, Mountainview, USA')
    restaurant10 = Restaurant(name='Classic Slices', address='505 Willow St, Brookside, USA')

    pizza1 = Pizza(name='Cheese', ingredients='Dough, Tomato Sauce, Cheese')
    pizza2 = Pizza(name='Pepperoni', ingredients='Dough, Tomato Sauce, Cheese, Pepperoni')
    pizza3 = Pizza(name='Vegetarian', ingredients='Dough, Tomato Sauce, Cheese, Mushrooms, Bell Peppers, Onions')
    pizza4 = Pizza(name='Margherita', ingredients='Dough, Tomato Sauce, Fresh Mozzarella, Basil')
    pizza5 = Pizza(name='Hawaiian', ingredients='Dough, Tomato Sauce, Cheese, Ham, Pineapple')
    pizza6 = Pizza(name='BBQ Chicken', ingredients='Dough, BBQ Sauce, Cheese, Chicken, Red Onion, Cilantro')
    pizza7 = Pizza(name='Supreme', ingredients='Dough, Tomato Sauce, Cheese, Pepperoni, Sausage, Mushrooms, Bell Peppers, Olives')
    pizza8 = Pizza(name='White Pizza', ingredients='Dough, Olive Oil, Garlic, Ricotta, Mozzarella, Spinach')
    pizza9 = Pizza(name='Mushroom Lovers', ingredients='Dough, Tomato Sauce, Cheese, Mushrooms, Truffle Oil')
    pizza10 = Pizza(name='Pesto Delight', ingredients='Dough, Pesto Sauce, Cheese, Cherry Tomatoes, Arugula')

    # Commit the data to the database
    db.session.add_all([
        restaurant1, restaurant2, restaurant3, restaurant4, restaurant5,
        restaurant6, restaurant7, restaurant8, restaurant9, restaurant10,
        pizza1, pizza2, pizza3, pizza4, pizza5, pizza6, pizza7, pizza8, pizza9, pizza10
    ])
    db.session.commit()

    # Create RestaurantPizza instances with prices
    restaurant_pizza1_1 = RestaurantPizza(restaurant=restaurant1, pizza=pizza1, price=15)
    restaurant_pizza1_2 = RestaurantPizza(restaurant=restaurant1, pizza=pizza2, price=20)
    restaurant_pizza2_2 = RestaurantPizza(restaurant=restaurant2, pizza=pizza2, price=25)
    restaurant_pizza3_3 = RestaurantPizza(restaurant=restaurant3, pizza=pizza3, price=18)
    restaurant_pizza4_4 = RestaurantPizza(restaurant=restaurant4, pizza=pizza4, price=22)
    restaurant_pizza5_5 = RestaurantPizza(restaurant=restaurant5, pizza=pizza5, price=21)
    restaurant_pizza6_6 = RestaurantPizza(restaurant=restaurant6, pizza=pizza6, price=24)
    restaurant_pizza7_7 = RestaurantPizza(restaurant=restaurant7, pizza=pizza7, price=28)
    restaurant_pizza8_8 = RestaurantPizza(restaurant=restaurant8, pizza=pizza8, price=26)
    restaurant_pizza9_9 = RestaurantPizza(restaurant=restaurant9, pizza=pizza9, price=20)
    restaurant_pizza10_10 = RestaurantPizza(restaurant=restaurant10, pizza=pizza10, price=23)

    # Commit the RestaurantPizza instances to the database
    db.session.add_all([
        restaurant_pizza1_1, restaurant_pizza1_2, restaurant_pizza2_2,
        restaurant_pizza3_3, restaurant_pizza4_4, restaurant_pizza5_5,
        restaurant_pizza6_6, restaurant_pizza7_7, restaurant_pizza8_8,
        restaurant_pizza9_9, restaurant_pizza10_10
    ])
    db.session.commit()

if __name__ == '__main__':
    from app import app

    with app.app_context():
        db.create_all()
        seed_data()

print("🦸‍♀️ Done seeding!")
