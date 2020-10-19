# #from 15:00 to 16:00

# import requests
# from requests.auth import AuthBase
# from requests.auth import HTTPBasicAuth
# import time
# import database

# start_time,end_time=database.reader("no7").split("-")

# auth = HTTPBasicAuth('soft3888', 'aK7is&jIn9O0s(')
# url="https://soft3888.ddns.net/rest/items/"

# headers = {
#     'Content-Type': 'text/plain'
#     }
# start_time_hour = int(start_time.split(":")[0])
# start_time_minute = int(start_time.split(":")[1])
# start_time_plus30 = str(start_time_hour)+":"+str(start_time_minute+30)

# while True:
#     time_now = time.strftime("%H:%M", time.localtime())
#     #when time equals to 15:00
#     if time_now == start_time:
#         requests.request("POST", url+"systemControl", headers=headers, data="OFF", auth=auth)
#         requests.request("POST", url+"ruleTest", headers=headers, data="ON", auth=auth)
#         requests.request("POST", url+"ruleTest", headers=headers, data="OFF", auth=auth)
        
#         #set light color (light bulbs and light strips)
#         colors = "160,0,100"
#         requests.request("POST", url+"lightBulbsColor", headers=headers, data=colors, auth=auth)
#         requests.request("POST", url+"lightStripsColor", headers=headers, data=colors, auth=auth)
        
#         #projector play workout video
#         data="https://api-soft3888.ddns.net/workout.mp4"
#         requests.request("POST", url+"chromecastPlay", headers=headers, data=data, auth=auth)
#         data="100"
#         requests.request("POST", url+"chromecastVolume", headers=headers, data=data, auth=auth)
#         time.sleep(61) 
#     #when time equals 15:30
#     elif time_now == start_time_plus30:
#         #play gym scene
#         data="https://media.self.com/photos/58e7dd9d3172253b0d06ff08/master/w_1600%2Cc_limit/Booty-Band-Side-Steps.gif"
#         requests.request("POST", url+"chromecastPlay", headers=headers, data=data, auth=auth)

#         #play workout music
#         data="https://request-soft3888.ddns.net/gym-sound"
#         requests.request("POST", url+"nestControl", headers=headers, data=data, auth=auth)

#     elif time_now == end_time: 
#         time.sleep(61) 