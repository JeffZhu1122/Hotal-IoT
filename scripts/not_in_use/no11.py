# from 20_21.rules

import json
import time
import database
import datetime
import configparser
from threading import Thread
import util

config = configparser.ConfigParser()
start_time,end_time=database.reader("no11").split("-")

light_hue = '35'
light_saturation = '50'

chromecastVolume_data = '50'
chromecastPlay_data = 'https://api-soft3888.ddns.net/campfire.mp4'
timer = 108.0

while True:
    time_now = time.strftime("%H:%M", time.localtime())

    if start_time == time_now:

        # Show a vivid campfire scene
        util.api_call("chromecastPlay", chromecastPlay_data)
        util.api_call("chromecastVolume", chromecastVolume_data)
        util.api_call("chromecastControl", "PLAY")
        
        # Light bulbs, strips fade out
        bulbs_brightness = 100
        strips_brightness = 100
        while True:
            if bulbs_brightness == 0:
                break
            bulbs_brightness = bulbs_brightness - 1
            strips_brightness = strips_brightness - 1
            bulbs_light_data = light_hue + light_saturation + bulbs_brightness
            strips_light_data = light_hue + light_saturation + strips_brightness
            util.api_call("lightBulbsColor", bulbs_light_data)
            util.api_call("lightStripsColor", strips_light_data)
            

            time.sleep(timer - ((time.time() - start_time) % timer))

        # strips_brightness = 100
        # while True:
        #     if  strips_brightness <= 1:
        #         break
        #     strips_brightness = strips_brightness - 5
        #     strips_light_data = light_hue + light_saturation + strips_brightness
        #     response_lightstrips = requests.request("POST", url+"lightStripColor", header=header,data=strips_light_data, auth=auth)

    elif time_now == end_time: 
        util.api_call("chromecastStop", "ON")
        time.sleep(61) 

