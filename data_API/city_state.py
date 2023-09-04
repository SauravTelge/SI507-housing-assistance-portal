import requests
import json
class city_search:
    """
    A class to search for cities and states based on a given query.
    
    Attributes
    ----------
    None
    
    Methods
    -------
    city_state(query: str) -> dict:
        Returns a dictionary containing information about cities and states matching the query.
    """
    def city_state(query):
        """
        Retrieve city and state information based on a given query.
        
        Parameters
        ----------
        query : str
            The search string to find matching cities and states.
            
        Returns
        -------
        dict
            A dictionary containing information about matching cities and states.
        """

        # Define the URL endpoint for the city and state search API
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