# Weather App
"""
Project Idea: Develop a simple weather application that fetches weather data from an API
and displays it to the user. You can represent weather data as objects.
Why It’s Great for Beginners: This project introduces you to the concept of data
encapsulation and interaction with external APIs.
"""

import requests

class WeatherData:
    def __init__(self,loc, api_key):
        self.location = loc
        self.api_key = api_key

        url = "https://api.weatherapi.com/v1/current.json"
        params = {
            "key": self.api_key,
            "q": loc
        }

        self.response = requests.get(url, params=params)

        try:
            self.data = self.response.json()
        except ValueError:
            print("Error parsing API response")
            self.data = {}

        self.success = self.response.status_code == 200
        if not self.success: print("Error:", self.response.status_code, self.response.text)


    def display(self):
        if self.success:
            print("Temperature:", self.data["current"]["temp_c"], "°C")
            print("Humidity:", self.data["current"]["humidity"], "%")
            print("Wind Speed:", self.data["current"]["wind_kph"], "kph")
            print("Condition:", self.data["current"]["condition"]["text"])




def main():
    location = input("Enter your location: ")
    key = input("Enter your API key: ")

    weather_data = WeatherData(location, key)
    weather_data.display()

main()
