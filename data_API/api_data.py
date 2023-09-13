import requests
import json
from time import sleep
from extra_files.save_file import readWriteFile

def api(url_query, querystring, key, host_name):
    """
    Sends a GET request to the specified URL with headers and query parameters.

    Parameters
    ----------
    url_query : str
        The URL to send the GET request to.
    querystring : dict
        Dictionary containing query parameters to be sent with the request.
    key : str
        The API key to be set in the 'X-RapidAPI-Key' header.
    host_name : str
        The hostname to be set in the 'X-RapidAPI-Host' header.

    Returns
    -------
    dict
        The JSON response received from the GET request.
    """
    url = url_query

    headers = {
        "content-type": "application/octet-stream",
        "X-RapidAPI-Key":key ,
        "X-RapidAPI-Host": host_name,
    }

    response = requests.get(url, headers=headers, params=querystring)

    response_json = response.json()
    return response_json

class apiData:
    """
    A class to search for cities and states based on a given query.

    Attributes
    ----------
    None

    Methods
    -------
    city_state(query: str) -> dict:
        Searches for cities and states based on a given query and returns a dictionary containing information 
        about the matching cities and states.

    house_info(city: str) -> dict:
        Fetches housing data for a specified city and returns a dictionary containing the housing data.

    save_housing_data() -> None:
        Retrieves housing data for a set of cities and saves the information to a JSON file. 

    weather_data(city: str, startdate: str, enddate: str) -> tuple:
        Retrieves both forecasted and historical weather data for a specified city and date range.
        Returns a tuple containing forecasted weather data and historical weather data in JSON format.
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
        querystring = {"q": f"{query}"}
        url = "https://city-and-state-search-api.p.rapidapi.com/cities/search"
        key ="3b22fa1263mshb51aa6ab6be___dummy___jsn10ddade3b058" 
        host_name = "city-and-state-search-api.p.rapidapi.com"
        response_city= api(url,querystring,key ,host_name) 
        
        return response_city
    
    def house_info(city):
        """
        Fetches housing data for a given city using the specified API key.

        Parameters
        ----------
        city : str
            The name of the city for which housing data is to be fetched.

        Returns
        -------
        dict
            A dictionary containing housing data for the specified city.
        """
        querystring = {"city_name": f"{city}", "country_name": "united states"}
        url = "https://cost-of-living-and-prices.p.rapidapi.com/prices"
        key = '74b52ccc3dmshc5135__dummy___5bbp16423ejsnf1ae02f6dcea'
        host_name = "cost-of-living-and-prices.p.rapidapi.com"

        reponse_housing = api(url,querystring, key,host_name)

        return reponse_housing
    
    def save_housing_data():
        """
        Saves housing data for a given city using the specified API key.

        Returns
        -------
        None
        """
        data = readWriteFile.readFile("./json_files/crimes.json")

        lst1, lst2, lst3, lst4, lst5, lst6, lst7 = [], [], [], [], [], [], []

        # Loop through a subset of the data (from index 58 to 61 inclusive)
        for i in range(58, 62):
            try:
                val = apiData.house_info(
                    data[i]["city name"]
                )

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

        # Writing the final data to a JSON file
        
        readWriteFile.writeFile("housing_list.json",dictt)

        return None
    
    def weather_data(city, startdate, enddate):
        """
        Fetches both forecasted and historical weather data for a given city and date range.

        Parameters
        ----------
        city : str
            The name of the city for which weather data is required.
        startdate : str
            The starting date for the historical data in 'YYYY-MM-DD' format.
        enddate : str
            The ending date for the historical data in 'YYYY-MM-DD' format.

        Returns
        -------
        tuple
            Contains two elements, the forecasted weather data and the historical weather data, both in JSON format.
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


   
        key = '74b52ccc3dmshc___dummy___09a5bbp16423ejsnf1ae02f6dcea'
        host_name = "visual-crossing-weather.p.rapidapi.com"

        reponse_history_weather = api(url_history,querystring_history, key,host_name)
        reponse_forecast_weather =  api(url_forecast,querystring_forecast, key,host_name)

        # store all the details in a JSON
        readWriteFile.writeFile("./json_files/response_forecast.json",reponse_forecast_weather)

        readWriteFile.writeFile("./json_files/response_history.json",reponse_history_weather)


        return (reponse_forecast_weather, reponse_history_weather)
    

