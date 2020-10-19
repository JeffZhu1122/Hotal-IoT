#from 9:30 AM to 10:30 AM

import requests
import json
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
import time
import database


raining_lightbulbs_colors = '26,100,52'
raining_lightstrip_colors = '26,90,10'

sunny_lightbulbs_colors = '190,100,22'
sunny_lightstrip_colors = 'OFF'

sunny_chromecastPlay_data = "https://api-soft3888.ddns.net/cafe_rain.mp4"
raining_chromecastPlay_data = "https://api-soft3888.ddns.net/cafe_day.mp4"
chromecastVolume_data = '100'


start_time,end_time=database.reader("no3").split("-")

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

        response_clouds = requests.get(url+'clouds').json()
        clouds_state = float(response_rain.get("state"))
        

        response_list = []

        """if raining"""
        if rain_state >= 0.0 or clouds_state >= 50.0 :
            lightbulbs_data = raining_lightbulbs_colors
            lightstrip_data = raining_lightstrip_colors
            response_lightbulbs = requests.request("POST", url+"lightBulbsColor", header=header, data=lightbulbs_data, auth=auth)
            response_lightstrip = requests.request("POST", url+"lightStripsColor", header=header, data="ON", auth=auth)
            response_lightstrip2 = requests.request("POST", url+"lightStripColor", header=header,data=lightstrip_data, auth=auth)
            response_chromecastPlay = requests.request("POST", url+"chromecastPlay", header=header, data=sunny_chromecastPlay_data, auth=auth)
            response_chromecastVolume = requests.request("POST",url+"chromecastVolume", header=header, data=chromecastVolume_data, auth=auth)
            response_chromecastControl = requests.request("POST", url+"chromecastControl", header=header, data="PLAY", auth=auth)

            
        else:
            lightbulbs_data = sunny_lightbulbs_colors
            lightstrip_data = sunny_lightstrip_colors
            response_lightbulbs = requests.request("POST", url+"lightBulbsColor", header=header, data=lightbulbs_data, auth=auth)
            response_lightstrip = requests.request("POST", url+"lightStripsColor", header=header, data="ON", auth=auth)
            response_lightstrip2 = requests.request("POST", url+"lightStripColor", header=header,data=lightstrip_data, auth=auth)
            response_chromecastPlay = requests.request("POST", url+"chromecastPlay", header=header, data=sunny_chromecastPlay_data, auth=auth)
            response_chromeastVolume = requests.request("POST",url+"chromecastVolume", header=header, data=chromecastVolume_data, auth=auth)
            response_chromecastControl = requests.request("POST", url+"chromecastControl", header=header, data="PLAY", auth=auth)

            




