from flask import Flask, render_template, request,Response
import os
import json
from data_access.tree import BSTNode
import string
from data_API.api_housing import housing
from data_API.api_weather import Weather
from datetime import date
import plotly
import plotly.express as px
import pandas as pd
import pickle

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
        # with open(f'tree_crimes.pickle', 'rb') as f:
        #     movie_tree = pickle.load(f)
        # # bst=BSTNode(data)
        # print(test_str)
        # val = movie_tree.exists(test_str)
        # print(val)
        # if val != False:
        #     city_rank =  float(val[0])
        #     city_crimes_per_day = float(val[1])
        #     state = val[2]

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
            print(test_str)
            print(postal)
            housing_data = housing.house(test_str,postal)
            today = date.today()
            weather_data_forecast,weather_data_history = Weather.weather_data(test_str,str(today.year-3)+'-'+str(today.month)+'-'+str(today.day)+"T00:00:00",str(today.year-3)+'-'+str(today.month+1)+'-'+str(today.day)+"T00:00:00")	
            data_temp,data_date = [],[]
            for i in range(len(weather_data_history['locations'][test_str]['values'])):
                
                data_temp.append(weather_data_history['locations'][test_str]['values'][i]['temp'])
                data_date.append(weather_data_history['locations'][test_str]['values'][i]['datetimeStr'])
                df = pd.DataFrame({
            'temp': data_temp,
            'date':data_date
        })
            fig = px.line(df, x='date', y='temp')
        
            graphJSON_history = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            data_temp,data_date = [],[]
            for i in range(len(weather_data_forecast['locations'][test_str]['values'])):
                
                data_temp.append(weather_data_forecast['locations'][test_str]['values'][i]['temp'])
                data_date.append(weather_data_forecast['locations'][test_str]['values'][i]['datetimeStr'])
            
            df = pd.DataFrame({
            'temp': data_temp,
            'date':data_date
        })
            fig = px.line(df, x='date', y='temp')
        
            graphJSON_forecast = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            

            

        
    return render_template('data.html',univname = univname,city_rank=city_rank,city_crimes_per_day=city_crimes_per_day,housing_data=housing_data,weather_data=weather_data_history,graphJSON_history =graphJSON_history,graphJSON_forecast=graphJSON_forecast)


if __name__ == "__main__":
    app.run(debug=True)