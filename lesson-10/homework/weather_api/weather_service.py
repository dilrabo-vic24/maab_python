import requests
from requests.exceptions import HTTPError, RequestException

def get_coordinates(city):
    GEO_URL = f"https://nominatim.openstreetmap.org/search?format=json&q={city}"
    
    try:
        response = requests.get(GEO_URL)
        response.raise_for_status()
        data = response.json()
        if data:
            return float(data[0]["lat"]), float(data[0]["lon"])
        else:
            print("City not found.")
            return None, None
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return None, None

def get_weather(city):
    API_KEY = "2c40b04f7ca9f214248b56914a321a81"
    lat, lon = get_coordinates(city)
    
    if lat is None or lon is None:
        return
    
    BASE_URL = "https://pro.openweathermap.org/data/2.5/forecast/climate"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric"
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        print_weather(data)
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

def print_weather(data):
    city = data.get("city", {}).get("name", "Unknown location")
    country = data.get("city", {}).get("country", "--")
    temp = data.get("list", [{}])[0].get("temp", {}).get("day", "--")
    humidity = data.get("list", [{}])[0].get("humidity", "--")
    pressure = data.get("list", [{}])[0].get("pressure", "--")
    description = data.get("list", [{}])[0].get("weather", [{}])[0].get("description", "--")
    
    print(f"\nWeather Information: {city}, {country}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure} hPa")
    print(f"Description: {description.capitalize()}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)