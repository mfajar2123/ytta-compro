import defaultTheme from "tailwindcss/defaultTheme";

/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./app.vue",
    "./error.vue",
  ],
  theme: {
    extend: {
      colors: {
        goldensand: '#D3A85F',
        blackobsidian: '#111111',
        darkamethyst: '#331432',
        whitedust: '#F8F4ED',
        lightamethyst: '#FFF3FD',
      },
      fontFamily: {
        sans: ["Raleway", ...defaultTheme.fontFamily.sans],
        heading: ["El Messiri", ...defaultTheme.fontFamily.sans],
      },
    },
  },
  plugins: [require("@tailwindcss/typography")],
};
