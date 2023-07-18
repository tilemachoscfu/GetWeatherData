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
    weather_data = get_weather_data(user_location)

    if 'error' in weather_data:
        print("Error:", weather_data['error']['message'])
    else:
        print(f"Weather in {weather_data['location']['name']}, {weather_data['location']['country']}:")
        print(f"Temperature: {weather_data['current']['temp_c']} °C")
        print(f"Description: {weather_data['current']['condition']['text']}")

        uv_index = weather_data['current']['uv']
        print(f"UV Index: {uv_index}")

        if uv_index >= 8:
            print("WARNING: The UV index is high. Please take appropriate preacautions.")

if __name__ == "__main__":
    main()
