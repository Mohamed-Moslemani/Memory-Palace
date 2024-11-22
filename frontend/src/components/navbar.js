// src/components/Navbar.jsx
import React from "react";
import { Link } from "react-router-dom";
import logo from "../assets/images/logo.png"; 

const Navbar = () => {
  return (
    <nav className="bg-primary text-secondary px-6 py-4 flex justify-between items-center">
      <Link to="/">
        <img src={logo} alt="Memory Palace Logo" style={{ height: "100px", width: "150px" }} 
        />
      </Link>
      <ul className="flex gap-6">
        <li>
          <Link to="/" className="hover:text-dark">
            Home
          </Link>
        </li>
        <li>
          <Link to="/login" className="hover:text-dark">
            Login/Signup
          </Link>
        </li>
        <li>
          <Link to="/api-docs" className="hover:text-dark">
            API Docs
          </Link>
        </li>
        <li>
          <Link to="/about" className="hover:text-dark">
            About
          </Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
