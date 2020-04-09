import requests
import json
import pprint
import calendar
# from datetime import datetime
# from dateutil import parser



data = requests.get('https://api.covid19india.org/data.json')
data = data.json()
TotalConfirmed = data["statewise"][0]["confirmed"]
TotalActive = data["statewise"][0]["active"]
TotalDeaths = data["statewise"][0]["deaths"]
TotalRecovered = data["statewise"][0]["recovered"]
LastUpdate = data["statewise"][0]["lastupdatedtime"]
# pprint.pprint(TotalConfirmed)
month = int(LastUpdate[4:5])
UpdateDate = LastUpdate[:2] + " " + calendar.month_name[month] + " " + LastUpdate[6:10] + " " + LastUpdate[11:13] + "00Hrs"
# datetime_object = LastUpdate.strptime('09/04/2020 15:05:29', '%d %m %Y %H:%M%:%S')
print(UpdateDate)
