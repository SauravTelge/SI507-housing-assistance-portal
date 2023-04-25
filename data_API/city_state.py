import requests
import json
class city_search:
    def city_state(query):
        url = "https://city-and-state-search-api.p.rapidapi.com/cities/search"

        querystring = {"q":f"{query}"}

        headers = {
            "content-type": "application/octet-stream",
            "X-RapidAPI-Key": "3b22fa1263mshb51aa6ab6be5039p122353jsn10ddade3b058",
            "X-RapidAPI-Host": "city-and-state-search-api.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        response_city = response.json()
        return response_city