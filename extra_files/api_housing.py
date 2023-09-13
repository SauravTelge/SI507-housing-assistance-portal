import requests
import json
from time import sleep
from extra_files.save_file import readWriteFile

class housing:
    """
    A class to represent housing-related operations.

    Attributes
    ----------
    None

    Methods
    -------
    house(city, varr):
        Fetches housing data for a given city using the specified API key.
    """

    def house(city, varr):
        """
        Fetches housing data for a given city using the specified API key.

        Parameters
        ----------
        city : str
            The name of the city for which housing data is to be fetched.
        varr : str
            The API key to be used for fetching the data.

        Returns
        -------
        dict
            A dictionary containing housing data for the specified city.
        """

        url = "https://cost-of-living-and-prices.p.rapidapi.com/prices"

        querystring = {"city_name": f"{city}", "country_name": "united states"}
        # key1= '74b52ccc3dmshc5135a0cc09a5bbp16423ejsnf1ae02f6dcea'
        # key2 = '0f836e441fmshf4cdccc8232af9cp1e5fedjsn9a65410fcd80'
        # key3 = '3b374677cbmshf6e6351ca7d60abp1155f1jsn2951405a43d0'

        # Setting up the headers for the API request
        headers = {
            "content-type": "application/octet-stream",
            "X-RapidAPI-Key": varr,
            "X-RapidAPI-Host": "cost-of-living-and-prices.p.rapidapi.com",
        }

        # Making the API request
        response = requests.get(url, headers=headers, params=querystring)
        # Converting the response to JSON format
        response = response.json()

        return response

    # with open("./json_files/crimes.json", "r") as myfile:
    #     data = json.load(myfile)
    
    
    # with open("housing_list3.json", "w") as myfile:
    #     myfile.write(json.dumps(dictt, indent=4))
