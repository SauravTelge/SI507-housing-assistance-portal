import requests
import json
from time import sleep


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

    with open("./json_files/crimes.json", "r") as myfile:
        data = json.load(myfile)

    lst1, lst2, lst3, lst4, lst5, lst6, lst7 = [], [], [], [], [], [], []

    # Loop through a subset of the data (from index 58 to 61 inclusive)
    for i in range(58, 62):
        try:
            val = house(
                data[i]["city name"],
                "3b374677cbmshf6e6351ca7d60abp1155f1jsn2951405a43d0",
            )
            print(i)

            # Appending specific price data to lists
            lst1.append(val["prices"][26]["avg"])
            lst2.append(val["prices"][35]["avg"])
            lst3.append(val["prices"][49]["avg"])
            lst4.append(val["prices"][51]["avg"])
            lst5.append(val["prices"][42]["avg"])
            lst6.append(val["prices"][48]["avg"])
            lst7.append(data[i]["city name"])

            # Sleep for 0.3 seconds to avoid hitting rate limits or for synchronization
            sleep(0.3)
        except:
            print("key error")
            continue

    # Prepare the final list of data
    final_list = []
    for i in range(len(lst1)):
        fin = [lst7[i], lst1[i], lst2[i], lst3[i], lst4[i], lst5[i], lst6[i]]
        final_list.append(fin)

    # Dictionary to store the final data
    dictt = {"data": final_list}
    final = {
        "city": lst7,
        "One bedroom apartment in city centre": lst1,
        "Meal in Inexpensive Restaurant": lst2,
        "Internet, 60 Mbps or More": lst3,
        "Dress in a Chain Store": lst4,
        "One-way Ticket, Local Transport": lst5,
        "Basic utilities": lst6,
    }

    print(dictt)

    # Writing the final data to a JSON file
    with open("housing_list3.json", "w") as myfile:
        myfile.write(json.dumps(dictt, indent=4))
