import React, { useState } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Navbar from "./components/navbar";
import Footer from "./components/footer";
import HomePage from "./pages/home"; // Example page
import LoginPage from "./pages/login"; // Example page
import SignupPage from "./pages/signup"; // Example page
import AboutPage from "./pages/about"; // Example page

const App = () => {
    const [isLoggedIn, setIsLoggedIn] = useState(false); // Manage login state

    return (
        <Router>
            <div className="app-container">
                <Navbar isLoggedIn={isLoggedIn} />
                <Routes>
                    <Route path="/home" element={<HomePage />} />
                    <Route path="/login" element={<LoginPage />} />
                    <Route path="/signup" element={<SignupPage />} />
                    <Route path="/about" element={<AboutPage />} />
                    {/* Add more routes here */}
                </Routes>
                <Footer />
            </div>
        </Router>
    );
};

export default App;
