from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Using free Open-Meteo API and a free geocoding API
GEOCODING_API_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/weather')
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    try:
        # Step 1: Geocoding (City name to coordinates)
        geo_params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }
        geo_response = requests.get(GEOCODING_API_URL, params=geo_params)
        geo_data = geo_response.json()

        if not geo_data.get('results'):
            return jsonify({"error": f"City '{city}' not found."}), 404

        location = geo_data['results'][0]
        lat = location['latitude']
        lon = location['longitude']
        city_name = location['name']
        country = location.get('country', '')

        # Step 2: Weather Data
        weather_params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": True,
            "timezone": "auto"
        }
        weather_response = requests.get(WEATHER_API_URL, params=weather_params)
        weather_data = weather_response.json()

        if 'current_weather' not in weather_data:
            return jsonify({"error": "Weather data could not be retrieved."}), 500

        current = weather_data['current_weather']
        
        # Open-Meteo WMO Weather interpretation codes
        # https://open-meteo.com/en/docs
        wmo_codes = {
            0: "Clear sky",
            1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
            45: "Fog", 48: "Depositing rime fog",
            51: "Light Drizzle", 53: "Moderate Drizzle", 55: "Dense Drizzle",
            61: "Slight Rain", 63: "Moderate Rain", 65: "Heavy Rain",
            71: "Slight Snow fall", 73: "Moderate Snow fall", 75: "Heavy Snow fall",
            77: "Snow grains",
            80: "Slight Rain showers", 81: "Moderate Rain showers", 82: "Violent Rain showers",
            85: "Slight Snow showers", 86: "Heavy Snow showers",
            95: "Thunderstorm",
            96: "Thunderstorm with slight hail", 99: "Thunderstorm with heavy hail"
        }
        
        weather_code = current.get('weathercode', 0)
        description = wmo_codes.get(weather_code, "Unknown")

        return jsonify({
            "city": f"{city_name}, {country}".strip(', '),
            "temperature": current.get('temperature'),
            "windspeed": current.get('windspeed'),
            "description": description
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
