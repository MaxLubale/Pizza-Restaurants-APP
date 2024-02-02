from app import db, Restaurant, Pizza, RestaurantPizza

def seed_data():
    # Create sample data
    restaurant1 = Restaurant(name='Sottocasa NYC', address='298 Atlantic Ave, Brooklyn, NY 11201')
    restaurant2 = Restaurant(name='PizzArte', address='69 W 55th St, New York, NY 10019')

    pizza1 = Pizza(name='Cheese', ingredients='Dough, Tomato Sauce, Cheese')
    pizza2 = Pizza(name='Pepperoni', ingredients='Dough, Tomato Sauce, Cheese, Pepperoni')

    # Commit the data to the database
    db.session.add_all([restaurant1, restaurant2, pizza1, pizza2])
    db.session.commit()

    # Create RestaurantPizza instances with prices
    restaurant_pizza1_1 = RestaurantPizza(restaurant=restaurant1, pizza=pizza1, price=15)
    restaurant_pizza1_2 = RestaurantPizza(restaurant=restaurant1, pizza=pizza2, price=20)
    restaurant_pizza2_2 = RestaurantPizza(restaurant=restaurant2, pizza=pizza2, price=25)

    # Commit the RestaurantPizza instances to the database
    db.session.add_all([restaurant_pizza1_1, restaurant_pizza1_2, restaurant_pizza2_2])
    db.session.commit()

if __name__ == '__main__':
    from app import app

    with app.app_context():
        db.create_all()
        seed_data()

print("🦸‍♀️ Done seeding!")
 