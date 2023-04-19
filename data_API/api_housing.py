import requests
import json


class housing:
		
	def house(city,postal):
		url = "https://cities-cost-of-living-and-average-prices-api.p.rapidapi.com/cost_of_living"

		querystring = {"country":"united-states","city":city+'-'+postal}

		headers = {
			"X-RapidAPI-Key": "74b52ccc3dmshc5135a0cc09a5bbp16423ejsnf1ae02f6dcea",
			"X-RapidAPI-Host": "cities-cost-of-living-and-average-prices-api.p.rapidapi.com"
		}

		response = requests.request("GET", url, headers=headers, params=querystring)
		response = response.json()

		return response

