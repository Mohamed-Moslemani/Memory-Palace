/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#FBF8EF",
        secondary: "#C9E6F0",
        accent: "#F96E2A",
        dark: "#78B3CE", // Repeated for consistency
      },
    },
  },
  plugins: [],
};
