import requests
import datetime
import os
import sys

def get_weather(latitude:float, longitude:float) -> dict:
    base_url = "https://api.open-meteo.com/v1/forecast"
    
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": ["temperature_2m", "relative_humidity_2m", "weather_code", "wind_speed_10m"],
        "timezone": "auto"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        data = response.json()
        current = data["current"]
        
        weather_codes = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Foggy",
            48: "Depositing rime fog",
            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Dense drizzle",
            61: "Slight rain",
            63: "Moderate rain",
            65: "Heavy rain",
            71: "Slight snow fall",
            73: "Moderate snow fall",
            75: "Heavy snow fall",
            95: "Thunderstorm",
        }
        
        weather_info = {
            "temperature": f"{current['temperature_2m']}°C",
            "humidity": f"{current['relative_humidity_2m']}%",
            "wind_speed": f"{current['wind_speed_10m']} km/h",
            "conditions": weather_codes.get(current['weather_code'], "Unknown"),
            "time": current['time']
        }
        
        return weather_info
        
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {e}"

def main():
    latitude = float(os.environ.get('LATITUDE', sys.argv[1] if len(sys.argv) > 1 else 40.7128))
    longitude = float(os.environ.get('LONGITUDE', sys.argv[2] if len(sys.argv) > 2 else -74.0060))
    
    print(f"Fetching weather data for {latitude}, {longitude}")
    weather_data = get_weather(latitude, longitude)
    
    if isinstance(weather_data, dict):
        print("\nCurrent Weather:")
        print(f"Time: {weather_data['time']}")
        print(f"Temperature: {weather_data['temperature']}")
        print(f"Humidity: {weather_data['humidity']}")
        print(f"Wind Speed: {weather_data['wind_speed']}")
        print(f"Conditions: {weather_data['conditions']}")
    else:
        print(weather_data)

if __name__ == "__main__":
    main()