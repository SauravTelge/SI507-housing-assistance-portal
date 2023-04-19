import requests
import json


class Weather:
    
    def weather_data(city,startdate,enddate):
            url_history = "https://visual-crossing-weather.p.rapidapi.com/history"
            querystring_history = {"startDateTime":startdate,"aggregateHours":"24","location":city,"endDateTime":enddate,"unitGroup":"us","dayStartTime":"8:00:00","contentType":"json","dayEndTime":"17:00:00","shortColumnNames":"0"}
 
            url_forecast = "https://visual-crossing-weather.p.rapidapi.com/forecast"
            querystring_forecast = {"aggregateHours":"24","location":city,"contentType":"json","unitGroup":"us","shortColumnNames":"0"}
            headers = {
				"X-RapidAPI-Key": "74b52ccc3dmshc5135a0cc09a5bbp16423ejsnf1ae02f6dcea",
				"X-RapidAPI-Host": "visual-crossing-weather.p.rapidapi.com"
			}
            response_forecast = requests.request("GET", url_forecast, headers=headers, params=querystring_forecast).json()
            
            response_history = requests.request("GET", url_history, headers=headers, params=querystring_history).json()
            
        
            return (response_forecast,response_history)
    
            

			
			

			

				

                
		
		

		

		