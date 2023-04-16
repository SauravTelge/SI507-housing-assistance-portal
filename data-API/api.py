import requests
import json

# url = "https://cities-cost-of-living-and-average-prices-api.p.rapidapi.com/cost_of_living"

# querystring = {"country":"united-states","city":"miami-fl"}

# headers = {
# 	"X-RapidAPI-Key": "74b52ccc3dmshc5135a0cc09a5bbp16423ejsnf1ae02f6dcea",
# 	"X-RapidAPI-Host": "cities-cost-of-living-and-average-prices-api.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)
# response = response.json()


# # store all the details in a JSON
# with open("housing.json", 'w') as myfile:
#     myfile.write(json.dumps(response,indent = 4))

url = "https://foreca-weather.p.rapidapi.com/location/search/miami"

querystring = {"lang":"en","country":"us"}

headers = {
	"X-RapidAPI-Key": "74b52ccc3dmshc5135a0cc09a5bbp16423ejsnf1ae02f6dcea",
	"X-RapidAPI-Host": "foreca-weather.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
response = response.json()

print(response['locations'][0]['id'])
# store all the details in a JSON
# with open("weather.json", 'w') as myfile:
#     myfile.write(json.dumps(response,indent = 4))