from flask import Flask, render_template, request,Response
import os
import json
from data_access.tree import BSTNode
import string
from data_API.api_housing import housing
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
        with open('crimes.json','r') as myfile:  
            data = json.load(myfile)  
        for i in range(len(data)):
            if test_str == data[i]['city name']:
                city_rank =  int(data[i]['City rank'])
                city_crimes_per_day = int(data[i]['Crimes per day'])
                state = data[i]['State']
        with open('postal.json','r') as myfile:  
            data = json.load(myfile)
        for i in range(len(data)):
            if data[i]['state'] == state:
                postal = data[i]['postal']
        response=housing.house(test_str,postal)
        

        

        
    return render_template('data.html',univname = test_str)


if __name__ == "__main__":
    app.run(debug=True)