// src/pages/APIDocs.jsx
import React from "react";

const APIDocs = () => {
  return (
    <div className="p-6 bg-gray-100 min-h-screen">
      <h1 className="text-3xl font-bold mb-4">API Documentation</h1>
      <p className="text-lg">Explore the Memory Palace API to integrate it into your projects.</p>
      <ul className="list-disc list-inside mt-6">
        <li><strong>POST /signup</strong> - Create a new user account.</li>
        <li><strong>POST /login</strong> - Login to your account and get an access token.</li>
        <li><strong>POST /save-password</strong> - Save a password for a service.</li>
        <li><strong>POST /retrieve-password</strong> - Retrieve a saved password.</li>
        <li><strong>POST /save-idea</strong> - Save an idea.</li>
        <li><strong>GET /retrieve-ideas</strong> - Retrieve all saved ideas.</li>
      </ul>
    </div>
  );
};

export default APIDocs;
