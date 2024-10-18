/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/templates/**/*.{html,js}"],
  theme: {
    extend: {
      colors:{
        primary:'#ff133e',
      },
      container: {
        screens: {
          sm: "100%",
          md: "100%",
          lg: "1024px",
          xl: "1280px",
        },
      },
    },
  },
  plugins: [],
}

