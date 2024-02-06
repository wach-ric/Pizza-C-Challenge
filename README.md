Flask Code Challenge - Pizza Restaurants
For this assessment, you'll be working with a Pizza Restaurant domain.
Note: You are required to come up with a fully built React frontend application, so you can test if your API is working. A fully functional front end will also be assessed for this code challenge.
Models
You need to create the following relationships:
- A `Restaurant` has many `Pizza`s through `RestaurantPizza`
- A `Pizza` has many `Restaurant`s through `RestaurantPizza`
- A `RestaurantPizza` belongs to a `Restaurant` and belongs to a `Pizza`
Validations
Add validations to the `RestaurantPizza` model:
- must have a `price` between 1 and 30
Routes
Set up the following routes. Make sure to return JSON data in the format specified along with the appropriate HTTP verb. 