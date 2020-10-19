#from 9:00 AM to 9:30 AM

import requests
import json
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
import time
import database


light_colors = '64,100,100'


raining_chromecastPlay_data = "https://api-soft3888.ddns.net/rain.mp4"
sunny_chromecastPlay_data = "https://api-soft3888.ddns.net/waterfall.mp4"
chromecastVolume_data = '50'


start_time,end_time=database.reader("no2").split("-")

auth = HTTPBasicAuth('soft3888', 'aK7is&jIn9O0s(')
url="https://soft3888.ddns.net/rest/items/"

header = {
    'Content-Type': 'text/plain',
    'Accept' : 'application/json'
    }
header_get = {
    'Accept' : 'application/json'
}


while True:
    time_now = time.strftime("%H:%M", time.localtime())

    if start_time == time_now:
        
        response_rain = requests.get(url+'rain').json()
        rain_state = float(response_rain.get("state"))

        if(rain_state >= 0.0):
            chromecastPlay_Data = raining_chromecastPlay_data
        else:
            chromecastPlay_Data = sunny_chromecastPlay_data

        response_list = []
        response_lightbulbs = requests.request("POST", url+"lightBulbsColor", header=header, data=light_colors, auth=auth)
        response_lightstrip = requests.request("POST", url+"lightStripsColor", header=header, data="ON", auth=auth)
        response_lightstrip2 = requests.request("POST", url+"lightStripColor", header=header,data=light_colors, auth=auth)
        response_chromecastPlay = requests.request("POST", url+"chromecastPlay", header=header, data=chromecastPlay_data, auth=auth)
        response_chromecastVolume = requests.request("POST",url+"chromecastVolume", header=header, data=chromecastVolume_data, auth=auth)
        response_chromecastControl = requests.request("POST", url+"chromecastControl", header=header, data="PLAY", auth=auth)

    elif time_now == end_time: 
        time.sleep(61) 