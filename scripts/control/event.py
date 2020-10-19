import json
import sys
sys.path.append('/etc/openhab2/scripts/control')
import time
import database
import datetime
import _thread
import util



class Event:

    def __init__(self, name, time_slot, actions):
        self.name = name
        self.start_time,self.end_time = time_slot.split("-")
        self.actions_list=json.loads(actions)
        # print(self.name, self.start_time,self.actions_list)

    def do_action(self):
        for key in self.actions_list.keys():
            if self.actions_list[key]["multhread"]=="fade":
                _thread.start_new_thread ( self.fade_light, (key,) )
            elif self.actions_list[key]["multhread"]=="movie":
                _thread.start_new_thread ( self.loop_movie, (key,) )
            elif self.actions_list[key]["multhread"]=="music":
                _thread.start_new_thread ( self.loop_music, (key,) )
            elif self.actions_list[key]["multhread"]=="None":
                if self.actions_list[key]["weather"]=="None":
                    util.api_call(key,self.actions_list[key]["command"])
                else:
                    rain=util.get_rain()
                    cloud=util.get_cloud()
                    if rain > 0.5 or cloud > 50:
                        util.api_call(key,self.actions_list[key]["weather"]["rainy"])
                    else:
                        util.api_call(key,self.actions_list[key]["weather"]["sunny"])

    def get_start(self):
        return self.start_time

    def fade_light(self,key):
        if self.actions_list[key]["fade_type"] == "color":
            util.api_call(key,self.actions_list[key]["command"])

            #fade in minutes
            fadein_min = int(self.actions_list[key]["fadein_min"])
            fadein_slot = int(self.actions_list[key]["fadein_slot"])
            hue_color = int(self.actions_list[key]["command"].split(",")[0])
            saturation = int(self.actions_list[key]["command"].split(",")[1])
            brightness = int(self.actions_list[key]["command"].split(",")[2])
            passed_minutes = 0

            while (passed_minutes < fadein_min):
                
                time.sleep(fadein_slot)
                hue_color=hue_color-1
                util.api_call(key,str(hue_color)+","+str(saturation)+","+str(brightness))
                    
                passed_minutes = passed_minutes + fadein_slot/60
            
        elif self.actions_list[key]["fade_type"] == "brightness":
            util.api_call(key,self.actions_list[key]["command"])

            #fade in minutes
            fadein_min = int(self.actions_list[key]["fadein_min"])
            fadein_slot = int(self.actions_list[key]["fadein_slot"])
            hue_color = int(self.actions_list[key]["command"].split(",")[0])
            saturation = int(self.actions_list[key]["command"].split(",")[1])
            brightness = int(self.actions_list[key]["command"].split(",")[2])
            passed_minutes = 0

            while (passed_minutes < fadein_min):
                time.sleep(fadein_slot)
                brightness=brightness+1
                util.api_call(key,str(hue_color)+","+str(saturation)+","+str(brightness))
                    
                passed_minutes = passed_minutes + fadein_slot/60

        elif self.actions_list[key]["fade_type"] == "out":
            util.api_call(key,self.actions_list[key]["command"])

            #fade in minutes
            fadein_min = int(self.actions_list[key]["fadein_min"])
            fadein_slot = int(self.actions_list[key]["fadein_slot"])
            hue_color = int(self.actions_list[key]["command"].split(",")[0])
            saturation = int(self.actions_list[key]["command"].split(",")[1])
            brightness = int(self.actions_list[key]["command"].split(",")[2])
            passed_minutes = 0

            while (passed_minutes < fadein_min):
                time.sleep(fadein_slot)
                brightness=brightness-1
                util.api_call(key,str(hue_color)+","+str(saturation)+","+str(brightness))
                    
                passed_minutes = passed_minutes + fadein_slot/60

    def loop_music(self,key):
        nest_play = ""
        nest_length = ""
        if self.actions_list[key]["command"] != "None":
            nest_play = self.actions_list.get(key).get("command")
            nest_length = self.actions_list.get("length")
            length_minutes, length_seconds= nest_length.split(":")
            total_length_seconds = float(length_seconds) + float(length_minutes * 60)
            while True:
                if self.end_time == time.strftime("%H:%M", time.localtime()):
                    break
                util.api_call(key,nest_play)
                time.sleep(total_length_seconds)
        # rain_state = self.weather().get("rain")
        # clouds_state = self.weather().get("clouds")
        if util.get_rain > 0.5 or util.get_cloud > 70:
            nest_play = self.actions_list.get(key).get("weather").get("rainy").get("url")
            nest_length = self.actions_list.get(key).get("weather").get("rainy").get("length")
            
            length_minutes, length_seconds= nest_length.split(":")
            total_length_seconds = float(length_seconds) + float(length_minutes * 60)
            
            
            while True:
                if self.end_time == time.strftime("%H:%M", time.localtime()):
                    break
                util.api_call(key,nest_play)
                time.sleep(total_length_seconds)
        else:
            nest_play = self.actions_list.get(key).get("weather").get("sunny").get("url")
            nest_length = self.actions_list.get(key).get("weather").get("sunny").get("length")
            
            length_minutes, length_seconds= nest_length.split(":")
            total_length_seconds = float(length_seconds) + float(length_minutes * 60)
            
            
            
            while True:
                if self.end_time == time.strftime("%H:%M", time.localtime()):
                    break
                util.api_call(key,nest_play)
                time.sleep(total_length_seconds)
        pass


    def loop_movie(self, key):
        chromecast_play = ""
        chromecast_length = ""
        if self.actions_list[key]["command"] != "None":
            chromecast_play = self.actions_list.get(key).get("command")
            chromecast_length = self.actions_list.get("length")
            length_minutes, length_seconds= chromecast_length.split(":")
            total_length_seconds = float(length_seconds) + float(length_minutes * 60)
            while True:
                if self.end_time == time.strftime("%H:%M", time.localtime()):
                    break
                util.api_call(key,chromecast_play)
                time.sleep(total_length_seconds)
        # rain_state = self.weather().get("rain")
        # clouds_state = self.weather().get("clouds")
        if util.get_rain > 0.5 or util.get_cloud > 70:
            chromecast_play = self.actions_list.get(key).get("weather").get("rainy").get("url")
            chromecast_length = self.actions_list.get(key).get("weather").get("rainy").get("length")
            
            length_minutes, length_seconds= chromecast_length.split(":")
            total_length_seconds = float(length_seconds) + float(length_minutes * 60)
            
            
            while True:
                if self.end_time == time.strftime("%H:%M", time.localtime()):
                    break
                util.api_call(key,chromecast_play)
                time.sleep(total_length_seconds)
        else:
            chromecast_play = self.actions_list.get(key).get("weather").get("sunny").get("url")
            chromecast_length = self.actions_list.get(key).get("weather").get("sunny").get("length")
            
            length_minutes, length_seconds= chromecast_length.split(":")
            total_length_seconds = float(length_seconds) + float(length_minutes * 60)
            
            
            
            while True:
                if self.end_time == time.strftime("%H:%M", time.localtime()):
                    break
                util.api_call(key,chromecast_play)
                time.sleep(total_length_seconds)
        pass
