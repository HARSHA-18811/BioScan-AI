/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        bio: {
          dark: "#0a0f1d",      // Dark navy background
          card: "#111827",      // Card dark slate
          cardborder: "#1e293b",
          teal: "#0d9488",      // Teal accent
          tealhover: "#0f766e",
          cyan: "#06b6d4",      // Cyan accent
          accent: "#14b8a6",
          emerald: "#10b981",
          muted: "#94a3b8",
        }
      }
    },
  },
  plugins: [],
}
