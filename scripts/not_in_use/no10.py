# from 19_20.rules

import json
import time
import database
import datetime
import configparser
import util

config = configparser.ConfigParser()
start_time,end_time=database.reader("no10").split("-")

chromecastVolume_data = '50'
chromecastControl_data = 'https://request-soft3888.ddns.net/movie'

comedy_strips_colour = "60,55,55" # yellow
fiction_strips_colour = "330,55,55" # pink
cartoon_strips_colour = "200,55,55" # blue

while True:
    time_now = time.strftime("%H:%M", time.localtime())
    
    if time_now == start_time:
            
        # Light bulbs off
        util.api_call("lightBulbsColor", "OFF")
        # Light strips on
        util.api_call("lightStripsColor", "ON")

        # Light strips colour for distinct genres
        if util.api_call("ComedySwitch", "ON"):
            util.api_call("FictionSwitch", "OFF")
            util.api_call("CartoonSwitch", "OFF")
            util.api_call("lightStripsColor", comedy_strips_colour)
        elif util.api_call("FictionSwitch","ON"):
            util.api_call("ComedySwitch", "OFF")
            util.api_call("CartoonSwitch", "OFF")
            util.api_call("lightStripsColor", fiction_strips_colour)
        else:
            util.api_call("ComedySwitch", "OFF")
            util.api_call("FictionSwitch", "OFF")
            util.api_call("lightStripsColor", cartoon_strips_colour)

        # Randomly play a movie from server files
        util.api_call("chromecastControl", "PLAY")
        util.api_call("chromecastVolume", chromecastVolume_data)
        util.api_call("chromecastControl", chromecastControl_data)
        

    
    elif time_now == end_time:
        
        lights_colour = "35,50,100" # orange
        
        # Projector & Movie stop 
        util.api_call("chromecastStop", "ON")
        # All light bulbs on
        util.api_call("lightBulbsColor", "ON")
        # Light bulbs, strips turn to orange
        util.api_call("lightBulbsColor", lights_colour)
        util.api_call("lightStripsColor", lights_colour)
