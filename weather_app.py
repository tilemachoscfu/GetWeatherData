import requests

def get_weather_data(location):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q": location}
    headers = {
        "X-RapidAPI-Key": "17c8fa9ae7mshde6981acfbf9481p17f37djsnf6af66af8cc1",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

def main():
    user_location = input("Enter the location (city name, country): ")
    user_temp_unit = input("Enter preffered temperature unit (C fot Celsius, F for Fahrenheit): ")

    if user_temp_unit.upper() not in ("C", "F"):
        print("Invalid temperature unit, Defaulting to Celsius (°C)")
        user_temp_unit = "C"
        
    weather_data = get_weather_data(user_location, user_temp_unit)

    if 'error' in weather_data:
        print("Error:", weather_data['error']['message'])
    else:
        print(f"Weather in {weather_data['location']['name']}, {weather_data['location']['country']}:")
        print(f"Temperature: {weather_data['current']['temp_c']} °C") if user_temp_unit.upper() == "C" else f"Temperature: {weather_data['current']['temp_f']} °F)
        print(f"Description: {weather_data['current']['condition']['text']}")

        uv_index = weather_data['current']['uv']
        print(f"UV Index: {uv_index}")

        if uv_index >= 8:
            print("WARNING: The UV index is high. Please take appropriate preacautions.")

if __name__ == "__main__":
    main()
