import bottle
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
from datetime import datetime
import time
import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
import json
import csv
import random
import os

alarm_dic={"bedtime":{"hour":None,"minute":None},"wakeuptime":{"hour":None,"minute":None}}

@bottle.route('/bedtime', method='POST')
def bedtime():
    today = datetime.date(datetime.now())
    repeat = 1
    hour = int(bottle.request.forms.get('bedtime-hour'))
    minute = int(bottle.request.forms.get('bedtime-minute'))
    
    if hour >= 24:
        hour -= 24
    if minute >= 60:
        hour += 1
        minute -= 60
    time = str(hour) + ":" + str(minute)

    global alarm_dic
    alarm_dic["bedtime"]["hour"]=hour
    alarm_dic["bedtime"]["minute"]=minute
    
    command = """
    send NightModeSwitch ON
    """

    event = {
        'summary': 'Bed Time',
        'description': command,
        'start': {
            'dateTime': '{}T{}:00+10:00'.format(today, time),
            'timeZone': 'Australia/Sydney',
        },
        'end': {
            'dateTime': '{}T{}:00+10:00'.format(today, time),
            'timeZone': 'Australia/Sydney',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT={}'.format(repeat) # occurs daily for count times
        ],
    }

    event = service.events().insert(calendarId='khkdpuhnpjk9lu5bu5988vubvo@group.calendar.google.com', body=event).execute()
    print ('Event created: %s' % (event.get('htmlLink')))
    return  bottle.redirect("https://api-soft3888.ddns.net/success.html")


@bottle.route('/wakeuptime', method='POST')
def wakeuptime():
    today = datetime.date(datetime.now())
    repeat = 1
    hour = int(bottle.request.forms.get('wakeuptime-hour')) - 1
    minute = int(bottle.request.forms.get('wakeuptime-minute')) + 30
    
    if hour < 0:
        hour += 24
    if hour >= 24:
        hour -= 24
    if minute >= 60:
        hour += 1
        minute -= 60
    time = str(hour) + ":" + str(minute)

    global alarm_dic
    alarm_dic["wakeuptime"]["hour"]=hour
    alarm_dic["wakeuptime"]["minute"]=minute
    
    command = """
    send WakeUpTestSwitch ON
    """

    event = {
        'summary': 'Wakeup Time',
        'description': command,
        'start': {
            'dateTime': '{}T{}:00+10:00'.format(today, time),
            'timeZone': 'Australia/Sydney',
        },
        'end': {
            'dateTime': '{}T{}:00+10:00'.format(today, time),
            'timeZone': 'Australia/Sydney',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT={}'.format(repeat) # occurs daily for count times
        ],
    }

    event = service.events().insert(calendarId='khkdpuhnpjk9lu5bu5988vubvo@group.calendar.google.com', body=event).execute()
    print ('Event created: %s' % (event.get('htmlLink')))
    return bottle.redirect("https://api-soft3888.ddns.net/success.html")


@bottle.route('/getalarm', method='GET')
def get_alarm():
    global alarm_dic
    return json.dumps(alarm_dic)

# @bottle.route('/movie', method='POST')
# def movie():
#     pass

@bottle.route('/music', method='POST')
def music():
    payload=bottle.request.forms.get("URL")

    auth = HTTPBasicAuth('soft3888', 'aK7is&jIn9O0s(')
    url = "https://soft3888.ddns.net/rest/items/Playuri"

    headers = {
    'Content-Type': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, data = payload,auth=auth)
    return bottle.redirect("https://api-soft3888.ddns.net/music.html")

@bottle.route('/movie',method='GET')
def movie():
    cat_list=["Comedy","Fiction","Cartoon"]
    payload=random.choice(cat_list)
    auth = HTTPBasicAuth('soft3888', 'aK7is&jIn9O0s(')
    url = "https://soft3888.ddns.net/rest/items/P_BR_Chromecast_URL"
    # url2 = "https://soft3888.ddns.net/rest/items/Playuri"
    url_category = "https://soft3888.ddns.net/rest/items/"


    with open('/www/wwwroot/api-soft3888.ddns.net/scripts/movielist.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    url_list = []
    for i in data:
        if payload.strip() == i[0].strip():
            print(payload)
            url_list = i[1:]

    headers = {
        'Content-Type': 'text/plain'
    }

    # response = requests.request("POST", url2, headers=headers, data=random.choice(url_list), auth=auth)
    # time.sleep(2)
    response = requests.request("POST", url, headers=headers, data=random.choice(url_list), auth=auth)
    response = requests.request("POST", url_category + payload, headers=headers, data="ON", auth=auth)
    return bottle.redirect("https://api-soft3888.ddns.net/movie.html")


@bottle.route('/michelin-sound',method='GET')
def michelin_sound():
    auth = HTTPBasicAuth('soft3888', 'aK7is&jIn9O0s(')

    headers = {
    'Content-Type': 'text/plain'
    }

    payload="https://api-soft3888.ddns.net/michelin-sound/"
    path = "/www/wwwroot/api-soft3888.ddns.net/html/michelin-sound"
    files = os.listdir(path)
    name=".DS_Store"
    while name==".DS_Store":
	    name=random.choice(files)
    url = "https://soft3888.ddns.net/rest/items/nestPlay"
    response = requests.request("POST", url, headers=headers, data = payload+name,auth=auth)

@bottle.route('/sunset-sound',method='GET')
def sunset_sound():
    auth = HTTPBasicAuth('soft3888', 'aK7is&jIn9O0s(')

    headers = {
    'Content-Type': 'text/plain'
    }

    payload="https://api-soft3888.ddns.net/sunset-sound/"
    path = "/www/wwwroot/api-soft3888.ddns.net/html/sunset-sound"
    files = os.listdir(path)
    name=".DS_Store"
    while name==".DS_Store":
	    name=random.choice(files)
    url = "https://soft3888.ddns.net/rest/items/nestPlay"
    response = requests.request("POST", url, headers=headers, data = payload+name,auth=auth)

@bottle.route('/gym-sound',method='GET')
def sunset_sound():
    auth = HTTPBasicAuth('soft3888', 'aK7is&jIn9O0s(')

    headers = {
    'Content-Type': 'text/plain'
    }

    payload="https://api-soft3888.ddns.net/gym-sound/"
    path = "/www/wwwroot/api-soft3888.ddns.net/html/gym-sound"
    files = os.listdir(path)
    name=".DS_Store"
    while name==".DS_Store":
	    name=random.choice(files)
    url = "https://soft3888.ddns.net/rest/items/nestPlay"
    response = requests.request("POST", url, headers=headers, data = payload+name,auth=auth)


credentials = pickle.load(open("/www/wwwroot/api-soft3888.ddns.net/scripts/token.pkl", "rb"))
service = build("calendar", "v3", credentials=credentials)
bottle.run(host='192.168.0.77', port=8000, debug=True)
