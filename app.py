from flask import Flask, render_template, request
import requests
import json
import calendar

app = Flask(__name__)

@app.route('/')
def index():
    data = requests.get('https://api.covid19india.org/data.json')
    data = data.json()
    TotalConfirmed = data["statewise"][0]["confirmed"]
    TotalActive = data["statewise"][0]["active"]
    TotalDeaths = data["statewise"][0]["deaths"]
    TotalRecovered = data["statewise"][0]["recovered"]
    LastUpdate = data["statewise"][0]["lastupdatedtime"]
    month = int(LastUpdate[4:5])
    UpdateDate = LastUpdate[:2] + " " + calendar.month_name[month] + " " + LastUpdate[6:10] + " " + LastUpdate[11:13] + "00Hrs"
    return render_template('index.html', totalConfirmed = TotalConfirmed, totalActive = TotalActive, totalDeaths = TotalDeaths, totalRecovered = TotalRecovered, lastUpdate = UpdateDate)
  

if __name__ == '__main__':
   app.run(debug = True)