from flask import Flask, render_template, request
import requests
import json
import calendar

app = Flask(__name__)

@app.route('/')
def index():
    data = requests.get('https://api.covid19india.org/data.json')
    data = data.json()
    LastUpdate = data["statewise"][0]["lastupdatedtime"]
    month = int(LastUpdate[4:5])
    UpdateDate = LastUpdate[:2] + " " + calendar.month_name[month] + " " + LastUpdate[6:10] + " " + LastUpdate[11:13] + ":00Hrs"
    return render_template('index.html', caseData = data['statewise'], lastUpdate = UpdateDate)
  

if __name__ == '__main__':
   app.run(debug = True)