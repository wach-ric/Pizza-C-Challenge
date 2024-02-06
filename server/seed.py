from app import app
import random
from models import db, Pizza, Restaurant, RestaurantPizza
from faker import Faker


with app.app_context():

    db.drop_all()
    db.create_all()

    fake = Faker()


    print("🍕 Seeding pizzas...")
    pizzas = [
        
        {
    "name": "Margherita",
    "ingredients": "Tomato sauce, Mozzarella cheese, Fresh basil"
  },
  {
    "name": "Pepperoni",
    "ingredients": "Tomato sauce, Mozzarella cheese, Pepperoni slices"
  },
  {
    "name": "Vegetarian",
    "ingredients": "Tomato sauce, Mozzarella cheese, Bell peppers, Mushrooms, Onions, Olives"
  },
  {
    "name": "Hawaiian",
    "ingredients": "Tomato sauce, Mozzarella cheese, Ham, Pineapple"
  },
  {
    "name": "Meat Lovers",
    "ingredients": "Tomato sauce, Mozzarella cheese, Pepperoni, Sausage, Bacon, Ground beef"
  },
  {
    "name": "BBQ Chicken",
    "ingredients": "Tomato sauce, Mozzarella cheese, BBQ sauce, Grilled chicken, Red onions, Cilantro"
  },
  {
    "name": "Supreme",
    "ingredients": "Tomato sauce, Mozzarella cheese, Pepperoni, Sausage, Mushrooms, Onions, Bell peppers, Olives"
  },
  {
    "name": "Four Cheese",
    "ingredients": "Tomato sauce, Mozzarella cheese, Cheddar cheese, Parmesan cheese, Gouda cheese"
  },
  {
    "name": "Mushroom Delight",
    "ingredients": "Creamy garlic sauce, Mozzarella cheese, Mushrooms, Caramelized onions, Thyme"
  },
  {
    "name": "Spinach and Feta",
    "ingredients": "Olive oil, Mozzarella cheese, Spinach, Feta cheese, Garlic"
  },
  {
    "name": "Buffalo Chicken",
    "ingredients": "Buffalo sauce, Mozzarella cheese, Grilled chicken, Red onions, Blue cheese crumbles"
  },
  {
    "name": "Pesto Paradise",
    "ingredients": "Pesto sauce, Mozzarella cheese, Cherry tomatoes, Pine nuts, Fresh basil"
  },
  {
    "name": "Mexican Fiesta",
    "ingredients": "Salsa, Mozzarella cheese, Ground beef, Jalapeños, Black beans, Corn, Avocado"
  },
  {
    "name": "White Garlic",
    "ingredients": "Olive oil, Mozzarella cheese, Garlic, Ricotta cheese, Fresh parsley"
  },
  {
    "name": "BBQ Bacon Ranch",
    "ingredients": "BBQ sauce, Mozzarella cheese, Bacon, Grilled chicken, Ranch dressing"
  },
  {
    "name": "Greek Delight",
    "ingredients": "Olive oil, Mozzarella cheese, Kalamata olives, Red onions, Feta cheese, Oregano"
  },
  {
    "name": "Vegan Veggie",
    "ingredients": "Tomato sauce, Vegan cheese, Bell peppers, Mushrooms, Onions, Zucchini, Spinach"
  },
  {
    "name": "Truffle Mushroom",
    "ingredients": "Truffle oil, Mozzarella cheese, Mushrooms, Parmesan cheese, Arugula"
  }
    ]
    for pizza_data in pizzas:
        pizza = Pizza(**pizza_data)
        db.session.add(pizza)

        
    print("🦸‍♀️ Seeding restaurants...")

    restaurants = []

    for i in range(20):
        restaurant = Restaurant(
            name=fake.company(),
            address=fake.address(),
        )
        restaurants.append(restaurant)

    db.session.add_all(restaurants)
    db.session.commit() 

    print("🇮🇹 Adding pizzas to restaurants...")
    
    for pizza in Pizza.query.all():
        for _ in range(random.randint(1, 3)):
            price = random.randint(1, 30)
            restaurant = Restaurant.query.order_by(db.func.random()).first()
            restaurant_pizzas = RestaurantPizza(pizza_id=pizza.id, restaurant_id=restaurant.id, price=price)
            db.session.add(restaurant_pizzas)

    db.session.commit()
    print("🦸‍♀️ Done seeding!")