import requests
# Replace with your actual Weatherstack API key
api_key = ""

def get_weather_data(location):

    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={location}"

    try:
        response = requests.get(url)
        response.raise_for_status()  

        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        return None

def display_weather(data):
    """Prints the weather information in a user-friendly format."""

    if data:
        location = data.get("location")
        current = data.get("current")
        print(f"Weather for {location.get('name')}:")
        print(f"Temperature: {current.get('temperature')}°C")
        print(f"Feels Like: {current.get('feelslike')}°C")
        print(f"Humidity: {current.get('humidity')}%")
        print(f"Weather Description: {current.get('weather_descriptions')[0]}")
        uv_index = current.get("uv_index")
        print(f"UV Index: {uv_index}")
    else:
        print("Weather data not available.")

if __name__ == "__main__":
    location = input("Enter a city or location: ")
    weather_data = get_weather_data(location)
    display_weather(weather_data)
