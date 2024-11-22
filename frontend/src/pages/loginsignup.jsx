import React, { useState } from "react";
import glassesOn from "../assets/images/glasses_on.svg"; 
import glassesOff from "../assets/images/glasses_off.svg"; 

const LoginSignup = () => {
  const [isLogin, setIsLogin] = useState(true);
  const [passwordVisible, setPasswordVisible] = useState(false);
  const [confirmPasswordVisible, setConfirmPasswordVisible] = useState(false);

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gradient-to-br from-primary to-secondary text-dark">
      <div className="bg-white p-8 rounded-lg shadow-lg w-96">
        <h2 className="text-4xl font-bold mb-6 text-center">
          {isLogin ? "Login" : "Signup"}
        </h2>
        <form>
          {!isLogin && (
            <input
              type="text"
              placeholder="Name"
              className="w-full mb-4 px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-accent"
            />
          )}
          <input
            type="email"
            placeholder="Email"
            className="w-full mb-4 px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-accent"
          />
          <div className="relative mb-4">
            <input
              type={passwordVisible ? "text" : "password"}
              placeholder="Password"
              className="w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-accent"
            />
            <img
              src={passwordVisible ? glassesOff : glassesOn}
              alt="Toggle Password Visibility"
              className="absolute right-3 top-3 h-6 w-6 cursor-pointer"
              onClick={() => setPasswordVisible(!passwordVisible)}
            />
          </div>
          {!isLogin && (
            <div className="relative mb-4">
              <input
                type={confirmPasswordVisible ? "text" : "password"}
                placeholder="Confirm Password"
                className="w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-accent"
              />
              <img
                src={confirmPasswordVisible ? glassesOff : glassesOn}
                alt="Toggle Confirm Password Visibility"
                className="absolute right-3 top-3 h-6 w-6 cursor-pointer"
                onClick={() => setConfirmPasswordVisible(!confirmPasswordVisible)}
              />
            </div>
          )}
          <button
            type="submit"
            className="w-full bg-accent text-white py-2 rounded-lg shadow-md hover:bg-dark hover:shadow-lg transition"
          >
            {isLogin ? "Login" : "Signup"}
          </button>
        </form>
        <p
          className="mt-4 text-accent text-center cursor-pointer hover:underline"
          onClick={() => setIsLogin(!isLogin)}
        >
          {isLogin
            ? "Don't have an account? Signup"
            : "Already have an account? Login"}
        </p>
      </div>
    </div>
  );
};

export default LoginSignup;
