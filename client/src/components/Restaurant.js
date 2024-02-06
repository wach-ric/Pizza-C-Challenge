import React, { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";

function Restaurant() {
  const [restaurantData, setRestaurantData] = useState({
    data: null,
    error: null,
    status: "pending",
  });

  const { id } = useParams();

  useEffect(() => {
    fetch(`/restaurants/${id}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Error: ${response.status} ${response.statusText}`);
        }
        return response.json();
      })
      .then((restaurant) => {
        setRestaurantData({ data: restaurant, error: null, status: "resolved" });
      })
      .catch((error) => {
        setRestaurantData({ data: null, error, status: "rejected" });
      });
  }, [id]);

  const { data: restaurant, error, status } = restaurantData;

  if (status === "pending") {
    return <h1>Loading...</h1>;
  }

  if (status === "rejected") {
    return <h1>{error.message}</h1>;
  }

  return (
    <section className="restaurant-section">
      <h2 className="restaurant-heading">{restaurant.name}</h2>
      <p className="restaurant-address">{restaurant.address}</p>

      <h3 className="restaurant-subheading">Pizzas:</h3>
      <ul className="restaurant-list">
        {restaurant.pizzas.map((pizza) => (
          <li key={pizza.id} className="restaurant-list-item">
            {pizza.name}
          </li>
        ))}
      </ul>

      <Link to="/restaurant_pizzas/new" className="restaurant-link">
        Add Restaurant Pizza
      </Link>
    </section>
  );
}

export default Restaurant;