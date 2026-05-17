# Aero | Premium Weather App 🌤️

A beautifully designed, full-stack weather application built with Python (Flask) and vanilla HTML/CSS/JavaScript. It features a modern, dark-mode glassmorphism interface with smooth animations and real-time weather data fetching.

This project was built to demonstrate solid Fullstack development fundamentals, including backend API routing, frontend asynchronous data fetching, and advanced CSS styling without relying on heavy frontend frameworks.

## ✨ Features

- **Real-Time Data**: Fetches live weather conditions (temperature, wind speed, weather descriptions) for any city worldwide.
- **Premium UI/UX**: Features a sleek, translucent glassmorphism card on top of an animated, deep-gradient background with floating orbs.
- **Responsive Design**: Looks great on both desktop and mobile devices.
- **Asynchronous Fetching**: Uses modern JavaScript (`fetch` API) to update the DOM dynamically without page reloads.
- **Zero-Dependency Frontend**: Built with pure HTML, CSS, and JS.
- **Free API Integration**: Utilizes the Open-Meteo API for both geocoding (translating city names to coordinates) and weather forecasting.

## 🛠️ Tech Stack

- **Backend**: Python 3, Flask, Requests
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **APIs**: [Open-Meteo API](https://open-meteo.com/) (Weather & Geocoding)
- **Typography & Icons**: Google Fonts (Outfit), FontAwesome

## 🚀 How to Run Locally

Follow these instructions to get the application running on your local machine.

### Prerequisites
Make sure you have [Python 3](https://www.python.org/downloads/) installed on your machine.

### Installation

1. **Clone or Download the Repository**
   Navigate to the project folder in your terminal:
   ```bash
   cd "Weather API"
   ```

2. **Install Dependencies**
   It's recommended to use a virtual environment, but you can install the required packages directly using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Flask Server**
   Run the backend application:
   ```bash
   python app.py
   ```

4. **View the App**
   Open your web browser and navigate to:
   ```text
   http://127.0.0.1:5000
   ```

## 📂 Project Structure

```text
Weather API/
│
├── app.py                  # Main Flask application and API routing
├── requirements.txt        # Python dependencies
│
├── templates/
│   └── index.html          # Main application layout and structure
│
└── static/
    ├── css/
    │   └── style.css       # Premium styles, animations, and glassmorphism
    └── js/
        └── script.js       # Asynchronous API fetching and DOM manipulation
```

## 🎓 Learning Outcomes

This project is an excellent demonstration of:
- Separating backend logic (API communication) from frontend presentation.
- Securely handling API requests on the server rather than exposing logic entirely on the client side.
- Creating high-end, modern web aesthetics using pure CSS keyframes, backdrop-filters, and gradients.
