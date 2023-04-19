import requests
import json


class Weather:
    
    def weather_data(city):
        url = f"https://foreca-weather.p.rapidapi.com/location/search/{city}"
        querystring = {"lang":"en","country":"us"}
        headers = {
			"X-RapidAPI-Key": "74b52ccc3dmshc5135a0cc09a5bbp16423ejsnf1ae02f6dcea",
			"X-RapidAPI-Host": "foreca-weather.p.rapidapi.com"
		}
        response = requests.request("GET", url, headers=headers, params=querystring)
        response = response.json()
        response['locations'][0]
        return None

		

                
		
		

		

		