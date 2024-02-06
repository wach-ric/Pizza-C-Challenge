import React, { useEffect, useState } from "react";
import { useNavigate } from 'react-router-dom';

function RestaurantPizza() {
  const [restaurants, setRestaurants] = useState([]);
  const [pizzas, setPizzas] = useState([]);
  const [restaurantId, setRestaurantId] = useState("");
  const [pizzaId, setPizzaId] = useState("");
  const [price, setPrice] = useState(0);
  const [formErrors, setFormErrors] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    fetch("/restaurants")
      .then((r) => r.json())
      .then(setRestaurants);
  }, []);

  useEffect(() => {
    fetch("/pizzas")
      .then((r) => r.json())
      .then(setPizzas);
  }, []);

  function handleSubmit(e) {
    e.preventDefault();
    const formData = {
      restaurant_id: restaurantId,
      pizza_id: pizzaId,
      price,
    };
    fetch("/restaurant_pizzas", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    }).then((r) => {
      if (r.ok) {
        navigate(`/restaurants/${restaurantId}`);
      } else {
        r.json().then((err) => setFormErrors(err.errors));
      }
    });
  }

  return (
    <form className="restaurant-pizza-form" onSubmit={handleSubmit}>
      <label htmlFor="pizza_id">Pizza:</label>
      <select
        id="pizza_id"
        name="pizza_id"
        value={pizzaId}
        onChange={(e) => setPizzaId(e.target.value)}
      >
        <option value="">Select a pizza</option>
        {pizzas.map((pizza) => (
          <option key={pizza.id} value={pizza.id}>
            {pizza.name}
          </option>
        ))}
      </select>
      <label htmlFor="restaurant_id">Restaurant:</label>
      <select
        id="restaurant_id"
        name="restaurant_id"
        value={restaurantId}
        onChange={(e) => setRestaurantId(e.target.value)}
      >
        <option value="">Select a restaurant</option>
        {restaurants.map((restaurant) => (
          <option key={restaurant.id} value={restaurant.id}>
            {restaurant.name}
          </option>
        ))}
      </select>
      <label htmlFor="price">Price:</label>
      <input
        type="number"
        id="price"
        name="price"
        value={price}
        onChange={(e) => setPrice(e.target.value)}
      />
      {formErrors.length > 0
        ? formErrors.map((err) => (
            <p key={err} className="form-error">
              {err}
            </p>
          ))
        : null}
      <button type="submit">Add Restaurant Pizza</button>
    </form>
  );
}

export default RestaurantPizza;