import React from "react";
import { Link } from "react-router-dom";

function Header() {
  return (
    <header className="header">
      <div className="center-container">
        <img src="/client/images/nastroeats.jpeg" alt="Restaurant Logo" className="logo" />
        <h1 className="title">
          <Link to="/" className="link">
            Restaurant Pizzas
          </Link>
        </h1>
      </div>
    </header>
  );
}

export default Header;