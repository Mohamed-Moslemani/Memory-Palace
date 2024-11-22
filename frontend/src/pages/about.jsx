import React from "react";

const About = () => {
  return (
    <div className="bg-primary min-h-screen flex items-center justify-center">
      <div className="max-w-4xl p-10 bg-white shadow-xl rounded-lg transform scale-105">
        {/* Header Section */}
        <h1 className="text-5xl font-extrabold text-accent mb-8 text-center">
          About <span className="text-secondary">Memory Palace</span>
        </h1>
        <p className="text-lg text-dark mb-6 leading-relaxed text-center">
          Welcome to <span className="font-semibold">Memory Palace</span>, your digital vault for securely storing and retrieving your ideas and passwords. 
          Designed to help you stay organized and focused, Memory Palace is the trusted companion for modern thinkers.
        </p>

        {/* Features Section */}
        <h2 className="text-3xl font-semibold text-green-700 mb-6">
          Why Choose Memory Palace?
        </h2>
        <ul className="list-disc list-inside text-lg text-gray-700 space-y-4 pl-5">
          <li>
            🔒 <span className="font-semibold text-accent">Advanced Security:</span> State-of-the-art encryption protects your most valuable information.
          </li>
          <li>
            🤖 <span className="font-semibold text-accent">AI-Powered Retrieval:</span> Find ideas or passwords instantly with intelligent search tools.
          </li>
          <li>
            📚 <span className="font-semibold text-accent">Organized Storage:</span> Create categories to structure your data for easy access.
          </li>
          <li>
            🌍 <span className="font-semibold text-accent">Global Access:</span> Access your secure vault from any device, anytime, anywhere.
          </li>
        </ul>

        {/* Vision Section */}
        <div className="mt-10">
          <h2 className="text-3xl font-semibold text-green-700 mb-4">
            Our Vision
          </h2>
          <p className="text-lg text-dark leading-relaxed">
            At Memory Palace, we believe in empowering individuals to focus on what matters most. By blending cutting-edge technology with intuitive design, our goal is to simplify your digital experience and give you peace of mind knowing your data is safe and accessible.
          </p>
        </div>

        {/* Call-to-Action Section */}
        <div className="mt-10 bg-secondary p-6 rounded-lg shadow-lg">
          <h2 className="text-3xl font-semibold text-dark mb-4">Get Started Today</h2>
          <p className="text-lg text-dark leading-relaxed mb-4">
            Join thousands of satisfied users who trust Memory Palace for their personal and professional needs. Sign up today and start building your secure memory palace.
          </p>
          <button className="bg-accent text-white px-6 py-3 rounded-lg shadow-md hover:bg-dark hover:text-secondary transition">
            Create Your Memory Palace
          </button>
        </div>
      </div>
    </div>
  );
};

export default About;
