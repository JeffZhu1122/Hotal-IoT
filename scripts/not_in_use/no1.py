#from 6:00 AM to 9:00 AM

import requests
import json
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
import time
import database
import datetime


light_hue = '60'
light_saturation = '0'

chromecastVolume_data = '50'
timer = 108.0


start_time,end_time=database.reader("no1").split("-")

auth = HTTPBasicAuth('soft3888', 'aK7is&jIn9O0s(')
url="https://soft3888.ddns.net/rest/items/"

header = {
    'Content-Type': 'text/plain',
    'Accept' : 'application/json'
    }
header_get = {
    'Accept' : 'application/json'
}

x = datetime.datetime.now()
month = int(x.strftime("%m"))

if month >= 3 and month <= 5:
    # Autumn
	chromecastPlay_data = "https://api-soft3888.ddns.net/autumn_sunrise.mp4"
elif month >= 6 and month <= 8:
    # Winter
    chromecastPlay_data = "https://api-soft3888.ddns.net/winter_sunrise.mp4"
elif month >= 9 and month <= 11:
    # Spring
    chromecastPlay_data = "https://api-soft3888.ddns.net/spring_sunrise.mp4"
else:
    # Summer
    chromecastPlay_data = "https://api-soft3888.ddns.net/summer_sunrise.mp4"

while True:
    time_now = time.strftime("%H:%M", time.localtime())

    if start_time == time_now:
        response_list = []
        response_chromecastPlay = requests.request("POST", url+"chromecastPlay", header=header, data=chromecastPlay_data, auth=auth)
        response_chromecastVolume = requests.request("POST",url+"chromecastVolume", header=header, data=chromecastVolume_data, auth=auth)
        response_chromecastControl = requests.request("POST", url+"chromecastControl", header=header, data="PLAY", auth=auth)
        response_lightstripOn = requests.request("POST", url+"lightStripsColor", header=header, data="ON", auth=auth)

        brightness = 0
        while True:
            if brightness == 50:
                break
            light_data = light_hue + light_saturation + brightness
            response_lightbulbs = requests.request("POST", url+"lightBulbsColor", header=header, data=light_data, auth=auth)
            response_lightstrips = requests.request("POST", url+"lightStripColor", header=header,data=light_data, auth=auth)

            time.sleep(timer - ((time.time() - start_time) % timer))

    elif time_now == end_time: 
        time.sleep(61) 