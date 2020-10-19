
#from 13_15.rule
import sys
sys.path.append('/etc/openhab2/scripts/control')
import time
import database
import util

start_time,end_time=database.reader("no6").split("-")

while True:
    time_now = time.strftime("%H:%M", time.localtime())
    
    if time_now == start_time:
            
        util.trun_off()

        colors = "180,0,100"
        util.api_call("lightBulbsColor",colors)
        util.api_call("lightStripsColor",colors)
        util.api_call("lightStripsColor","ON")

        data="https://api-soft3888.ddns.net/black.png"
        util.api_call("chromecastPlay",data)

        time.sleep(61) 
