import requests
import json

url = "https://cities-cost-of-living-and-average-prices-api.p.rapidapi.com/cost_of_living"

querystring = {"country":"united-states","city":"austin-tx"}

headers = {
	"X-RapidAPI-Key": "74b52ccc3dmshc5135a0cc09a5bbp16423ejsnf1ae02f6dcea",
	"X-RapidAPI-Host": "cities-cost-of-living-and-average-prices-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

import requests

url = "https://foreca-weather.p.rapidapi.com/location/search/mumbai"

querystring = {"lang":"en","country":"in"}

headers = {
	"X-RapidAPI-Key": "74b52ccc3dmshc5135a0cc09a5bbp16423ejsnf1ae02f6dcea",
	"X-RapidAPI-Host": "foreca-weather.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)