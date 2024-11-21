import React from "react";
import "./home.css";

const HomePage = () => {
    return (
        <div className="home">
            <div className="home-content">
                <h1>Welcome to Brainstormer</h1>
                <p>Your personalized memory palace for ideas and passwords.</p>
                <a href="/signup" className="cta-button">
                    Get Started
                </a>
            </div>
        </div>
    );
};

export default HomePage;
