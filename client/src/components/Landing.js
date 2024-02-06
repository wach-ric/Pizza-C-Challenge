import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function Landing() {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    fetch("/restaurants")
      .then((r) => r.json())
      .then(setRestaurants);
  }, []);

  function handleDelete(id) {
    fetch(`/restaurants/${id}`, {
      method: "DELETE",
    }).then((r) => {
      if (r.ok) {
        setRestaurants((restaurants) =>
          restaurants.filter((restaurant) => restaurant.id !== id)
        );
      }
    });
  }

  return (
    <section className="home-section">
      <h2 className="home-heading">All Restaurants</h2>
      <ul className="home-list">
        {restaurants.map((restaurant) => (
          <li key={restaurant.id} className="home-list-item">
            <Link to={`/restaurants/${restaurant.id}`} className="home-link">
              {restaurant.name}
            </Link>
            <button onClick={() => handleDelete(restaurant.id)} className="delete-button">
              Delete Restaurant
            </button>
          </li>
        ))}
      </ul>
    </section>
  );
}

export default Landing;