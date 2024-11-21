import React from "react";
import { Link } from "react-router-dom";
import "./navbar.css";

const Navbar = ({ isLoggedIn }) => {
    return (
        <nav className="navbar">
            <div className="nav-container">
                {/* Logo */}
                <div className="nav-left">
                    <Link to="/home" className="logo">
                        Brainstormer
                    </Link>
                </div>

                {/* Navigation Links */}
                <div className="nav-right">
                    {!isLoggedIn ? (
                        <>
                            <Link to="/login" className="nav-link">
                                Login
                            </Link>
                            <Link to="/signup" className="nav-link">
                                Signup
                            </Link>
                        </>
                    ) : (
                        <>
                            <Link to="/about" className="nav-link">
                                About Us
                            </Link>
                            <Link to="/api" className="nav-link">
                                API
                            </Link>
                            <Link to="/memory-palace" className="nav-link">
                                Your Memory Palace
                            </Link>
                        </>
                    )}
                </div>
            </div>
        </nav>
    );
};

export default Navbar;
