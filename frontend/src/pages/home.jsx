import React, { useState, useEffect } from "react";
import bgImage from "../assets/images/bg.png";

const Home = () => {
  const [animate, setAnimate] = useState(false);

  useEffect(() => {
    // Trigger animation on page load
    setTimeout(() => setAnimate(true), 100); // Small delay for smooth animation
  }, []);

  return (
    <div
      className="min-h-screen flex items-center justify-center bg-cover bg-center relative text-white"
      style={{
        backgroundImage: `url(${bgImage})`,
        backgroundAttachment: "fixed",
      }}
    >
      {/* Dark Gradient Overlay */}
      <div className="absolute inset-0 bg-gradient-to-b from-black/60 to-black/40"></div>

      {/* Content Section */}
      <div className="relative z-10 max-w-4xl text-center p-6 sm:p-10 md:p-20">
        <h1
          className={`text-5xl md:text-6xl font-extrabold mb-6 leading-tight transition-all duration-1000 ease-out ${
            animate ? "opacity-100 translate-y-0" : "opacity-0 translate-y-10"
          }`}
        >
          Welcome to <span className="text-secondary">Memory Palace</span>
        </h1>
        <p
          className={`text-lg md:text-xl mb-8 leading-relaxed transition-all duration-1000 ease-out delay-200 ${
            animate ? "opacity-100 translate-y-0" : "opacity-0 translate-y-10"
          }`}
        >
          Your ultimate tool for securely storing and retrieving ideas and passwords. 
          Stay organized, stay secure, and make life effortless.
        </p>
        <button className="bg-accent text-white px-8 py-4 rounded-lg shadow-lg hover:bg-dark hover:text-secondary transition text-lg">
          Get Started
        </button>
      </div>
    </div>
  );
};

export default Home;
