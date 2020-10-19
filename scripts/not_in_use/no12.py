#from 9:00 PM to 6:00 AM

import requests
import json
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
import time
import database


light_colors = '60,100,10'
chromecastPlay_data = 'https://api-soft3888.ddns.net/stars.gif'
nestPlay_data = 'https://api-soft3888.ddns.net/moonlight.mp3'
nestVolume_data = '20'

timer = 360.0


start_time,end_time=database.reader("no12").split("-")

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
        response_list = []
        response_lightbulbs = requests.request("POST", url+"lightBulbsColor", header=header, data="OFF", auth=auth)
        response_lightstrip = requests.request("POST", url+"lightStripsColor", header=header, data="ON", auth=auth)
        response_lightstrip2 = requests.request("POST", url+"lightStripColor", header=header,data=light_colors, auth=auth)
        response_chromecastPlay = requests.request("POST", url+"chromecastPlay", header=header, data=chromecastPlay_data, auth=auth)
        response_chromecastControl = requests.request("POST", url+"chromecastControl", header=header, data="PLAY", auth=auth)
        response_nestPlay = requests.request("POST", url+"nestPlay", header=header, data=nestPlay_data, auth=auth)
        reponse_nestVolume = requests.request("POST", url+"nestVolume", header=header, data=nestVolume_data, auth=auth)
        response_nestControl = requests.request("POST", url+"nestControl", header=header, data="PLAY", auth=auth)

        while True:
            current_time = time.strftime("%H:%M", time.localtime())
            if current_time >= end_time:
                break
            response_nestPlay = requests.request("POST", url+"nestPlay", header=header, data=nestPlay_data, auth=auth)
            reponse_nestVolume = requests.request("POST", url+"nestVolume", header=header, data=nestVolume_data, auth=auth)
            response_nestControl = requests.request("POST", url+"nestControl", header=header, data="PLAY", auth=auth)    
            time.sleep(timer - ((time.time() - start_time) % timer))
        
    elif time_now == end_time: 
        time.sleep(61) 