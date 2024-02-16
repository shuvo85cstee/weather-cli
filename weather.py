#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from quo import echo
import requests, os, sys

# Export openweather key as OPENWEATHER_API_KEY environment variable
if "OPENWEATHER_API_KEY" not in os.environ:
    print("Please export openweather api key as OPENWEATHER_API_KEY environment variable")
    sys.exit()
else:
    key = os.environ.get("OPENWEATHER_API_KEY")

# Base URL for openweather
baseUrl = "https://api.openweathermap.org/data/2.5/weather?"

# locations I am interest to know
loc = ["Dhaka", "Berlin", "Copenhagen"]

for i in loc:
    echo(f"\n{i}", bold=True)
    # Create url for requests from server
    url = baseUrl + "appid=" + key + "&q=" + i

    # Store api response
    response = requests.get(url)

    # Parse data in json format for consume
    res = response.json()

    # Check whether or not the city was found
    if res["cod"] == "404":
        print(" Location Not Found ")
    else:
        # Gets temperature in Kelvin
        tempK = res["main"]["temp"]
        # Gets the real feel of the weather
        feelK = res["main"]["feels_like"]
        # Gets humidity in percentage
        humi = res["main"]["humidity"]
        # Gets weather description
        desc = res["weather"][0]["description"]

        # Converting temperatures from Kelvin to Celcius
        tempC = tempK - 273.15
        feelC = feelK - 273.15

        # Output weather details
        print("Temperature = " + str(round(tempC, 2)) + " °C")
        print("Feels Like = " + str(round(feelC, 2)) + " °C")
        print("Humidity = " + str(humi) + " %")
        print("Description = " + str(desc))

        #Runs the shell command to get weather information from wttr.in. Thanks to Igor chubin
        print(os.popen(f"curl wttr.in/{i} --no-progress-meter").read())
