import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        # Parse weather data
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Display weather details
        print(f"Weather in {city_name.capitalize()}:\n")
        print(f"Description: {weather_description.capitalize()}")
        print(f"Temperature: {temperature}°C (Feels like: {feels_like}°C)")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

    #Use of except handler in case of errors
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except KeyError:
        print("City not found or API response format changed.")

if __name__ == "__main__":
    print("Welcome to the Weather App!")
    # Use of API key from Openweathermap.website
    api_key = "f59c7b870b8ac6931c21ba38caccd96c"
    city_name = input("Enter city: ")  
    get_weather(city_name, api_key)
