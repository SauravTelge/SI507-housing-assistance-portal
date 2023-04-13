from flask import Flask, render_template, request,Response
import os

app = Flask(__name__)

@app.route("/")  
def home():
    return render_template("index.html")

@app.route("/data")
def results():
    if request.method == "POST":
        univname = request.form['uniname']
        print(univname)
    return render_template('data.html',univname = univname)


if __name__ == "__main__":
    app.run(debug=True)