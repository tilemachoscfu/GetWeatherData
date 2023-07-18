Weather Data Retrieval Script

This Python script fetches weather data for a specific location using the WeatherAPI.com API through RapidAPI. It displays the temperature, weather description, and UV index for the provided location. If the UV index is high (8 or above), it will display a warning message advising the user to take precautions.

Prerequisites
Python 3.x
requests library
You need Python 3.x installed on your machine to run this script. If you don't have it, you can download it from the official Python website: https://www.python.org/downloads/

To install the required requests library, run the following command:

pip install requests

Getting Started
Clone the repository or download the weather_app.py file directly.
Open a terminal or command prompt and navigate to the folder where weather_app.py is located.
Usage
Run the script using the following command:

python weather_app.py

Enter the location for which you want to fetch the weather data. For example, you can type "London, UK" or any other city name and country.

The script will make an API call to the WeatherAPI.com API and display the current weather data for the specified location.

API Key
The script uses an API key to access the WeatherAPI.com API through RapidAPI. The API key is already included in the script as a header. If you encounter any issues related to the API, please check if the API key is valid or consider generating a new one from the RapidAPI website: https://rapidapi.com/weatherapi/api/weatherapi-com/

UV Index Warning
The script checks the UV index value returned by the API. If the UV index is 8 or above, it will display a warning message indicating that the UV index is high and advising the user to take precautions.

Authors
Tilemachos Zoitsas
