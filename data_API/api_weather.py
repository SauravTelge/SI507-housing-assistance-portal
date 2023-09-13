import requests
import json

"""
This module provides functionality to fetch weather data (both historical and forecasted)
from the Visual Crossing Weather API for a given city and date range.
"""


class Weather:
    """
    Represents a utility for fetching weather data.
    """

    def weather_data(city, startdate, enddate):
        """
        Fetches both forecasted and historical weather data for a given city and date range.

        Parameters:
        - city (str): The name of the city for which weather data is required.
        - startdate (str): The starting date for the historical data in 'YYYY-MM-DD' format.
        - enddate (str): The ending date for the historical data in 'YYYY-MM-DD' format.

        Returns:
        tuple: Contains two elements, the forecasted weather data and the historical weather data, both in JSON format.
        """
        url_history = "https://visual-crossing-weather.p.rapidapi.com/history"
        querystring_history = {
            "startDateTime": startdate,
            "aggregateHours": "24",
            "location": city,
            "endDateTime": enddate,
            "unitGroup": "us",
            "dayStartTime": "8:00:00",
            "contentType": "json",
            "dayEndTime": "17:00:00",
            "shortColumnNames": "0",
        }

        url_forecast = "https://visual-crossing-weather.p.rapidapi.com/forecast"
        querystring_forecast = {
            "aggregateHours": "24",
            "location": city,
            "contentType": "json",
            "unitGroup": "us",
            "shortColumnNames": "0",
        }
        headers = {
            "X-RapidAPI-Key": "74b52ccc3dmshc5135a0cc09a5bbp16423ejsnf1ae02f6dcea",
            "X-RapidAPI-Host": "visual-crossing-weather.p.rapidapi.com",
        }
        response_forecast = requests.request(
            "GET", url_forecast, headers=headers, params=querystring_forecast
        )

        response_history = requests.request(
            "GET", url_history, headers=headers, params=querystring_history
        )
        response_forecast = response_forecast.json()

        response_history = response_history.json()
        # store all the details in a JSON
        with open("./json_files/response_forecast.json", "w") as myfile:
            myfile.write(json.dumps(response_forecast, indent=4))
            # store all the details in a JSON
        with open("./json_files/response_history.json", "w") as myfile:
            myfile.write(json.dumps(response_history, indent=4))

        return (response_forecast, response_history)
