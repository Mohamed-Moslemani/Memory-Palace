// src/App.js
import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Navbar from "./components/navbar";
import Home from "./pages/home";
import LoginSignup from "./pages/loginsignup";
import APIDocs from "./pages/apidocs";
import About from "./pages/about";

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<LoginSignup />} />
        <Route path="/api-docs" element={<APIDocs />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Router>
  );
}

export default App;
