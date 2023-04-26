from flask import Flask, render_template, request
import json
import string
from data_API.api_weather import Weather
from datetime import date
import plotly
import plotly.express as px
import pandas as pd
import pickle
from data_API.city_state import city_search

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/crime_stats")
def crime_stats():
    with open('crimes_new.json','r') as myfile:  
            data1 = json.load(myfile) 
    return render_template("crime.html",data1=data1)

@app.route("/housing_stats")
def housing_stats():
    return render_template("datatables.html")

# @app.route("/crime", methods=['GET'])  
# def crime_show():
#     return render_template("qs.html",job_role=job_role)

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

        with open('crimes_new.json','r') as myfile:  
            data = json.load(myfile) 

        for i in range(len(data)):
            if test_str == data[i]['city name'].strip():
                city_rank =  float(data[i]['City rank'])
                city_crimes_per_day = float(data[i]['Crimes per day'])
                state = data[i]['State']
                break
            else:
                city_rank = 'No data available'
                city_crimes_per_day = 'No data available'
                state = 'No data available'


        if state == 'No data available':
            val=city_search.city_state(test_str)
        else:
            # with open('postal.json','r') as myfile:  
            #     data = json.load(myfile)
            # for i in range(len(data)):
            #     if data[i]['state'] == state:
            #         postal = data[i]['postal']
            # print(test_str)
            # print(postal)
            
        
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

    return render_template('data.html',univname = univname,city_rank=city_rank,test_str=test_str,city_crimes_per_day=city_crimes_per_day,weather_data=weather_data_history,graphJSON_history =graphJSON_history,graphJSON_forecast=graphJSON_forecast)



@app.route("/data_crime",methods=["GET", "POST"])  
def crime():
    if request.method == "POST":
        crime =(request.form['crime']).strip() 
        crime = int(crime)
        with open('crimes.json','r') as myfile:  
            data = json.load(myfile) 
        with open(f'tree_crimes.pickle', 'rb') as f:
            crime_tree = pickle.load(f)
      
        val = crime_tree.exists(crime)
        print(val)
        if val != False:
            city =  val[0]
            city_crimes_per_day = float(val[1])
            state = val[2]
            
    return render_template("results.html",city=city, city_crimes_per_day=city_crimes_per_day,state=state,crime=crime)


if __name__ == "__main__":
    app.run(debug=True)