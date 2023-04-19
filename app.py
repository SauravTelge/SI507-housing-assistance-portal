from flask import Flask, render_template, request,Response
import os
import json
from data_access.tree import BSTNode
import string
from data_API.api_housing import housing
from data_API.api_weather import Weather
from datetime import date

app = Flask(__name__)

@app.route("/")  
def home():
    return render_template("index.html")

@app.route("/data",methods=["GET", "POST"])
def results():
    if request.method == "POST":
        univname = request.form['uniname']
        with open('universities.json','r') as myfile:  
            data = json.load(myfile)  
        for i in range(len(data)):
            if univname == data[i]['university name']:
                univcity =  data[i]['university town']
    
         
        test_str = univcity.translate(str.maketrans('', '', string.punctuation))   
        test_str = test_str.strip()     
        with open('crimes.json','r') as myfile:  
            data = json.load(myfile)  
 
        for i in range(len(data)):
           
            if test_str == data[i]['city name'].strip():
                print('yes')
                city_rank =  float(data[i]['City rank'])
                city_crimes_per_day = float(data[i]['Crimes per day'])
                state = data[i]['State']
                break
            else:
                city_rank = 'No data available'
                city_crimes_per_day = 'No data available'
                state = 'No data available'
        if state == 'No data available':
            housing_data = 'No data available'
            weather_data = 'No data available'

        else:
            with open('postal.json','r') as myfile:  
                data = json.load(myfile)
            for i in range(len(data)):
                if data[i]['state'] == state:
                    postal = data[i]['postal']
            housing_data = housing.house(test_str,postal)
            
            today = date.today()

            
            weather_data = Weather.weather_data('ann arbor',str(today.year-3)+'-'+str(today.month)+'-'+str(today.day)+"T00:00:00",str(today)+"T00:00:00")	

        
    return render_template('data.html',univname = test_str,city_rank=city_rank,city_crimes_per_day=city_crimes_per_day,housing_data=housing_data,weather_data=weather_data)


if __name__ == "__main__":
    app.run(debug=True)