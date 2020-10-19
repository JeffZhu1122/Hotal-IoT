import configparser
import requests
import time
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

def read_config():
    config = configparser.ConfigParser()
    config.read('/etc/openhab2/scripts/control/config.ini')
    # config.read('config.ini')
    return config

def turn_off():
    api_call("systemControl","OFF")
    api_call("ruleTest","ON")
    api_call("ruleTest","OFF")
    time.sleep(1) 

def api_call(item,command):
    auth = HTTPBasicAuth('soft3888', 'aK7is&jIn9O0s(')
    config=read_config()
    url=config['SETTING']['root_url']+"/rest/items/"
    headers = {
            'Content-Type': 'text/plain'
            }
    requests.request("POST", url+item, headers=headers, data=command, auth=auth)
    
def get_rain():
    CITY_ID = "2147714"
    API_KEY = "4a3ea912a0624b7da97e09d6551e3d7e"
    URL = "http://api.weatherbit.io/v2.0/current?city_id={}&key={}".format(CITY_ID, API_KEY)
    response = requests.get(URL)
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()['data'][0]
        rain = data['precip']
        return rain
    else:
        # showing the error message
        print("Error in the HTTP request to {} with status code {}".format(URL, response.status_code))

def get_cloud():
    CITY_ID = "2147714"
    API_KEY = "4a3ea912a0624b7da97e09d6551e3d7e"
    URL = "http://api.weatherbit.io/v2.0/current?city_id={}&key={}".format(CITY_ID, API_KEY)
    response = requests.get(URL)
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()['data'][0]
        cloud = data['clouds']
        rain = data['precip']
        return cloud
    else:
        # showing the error message
        print("Error in the HTTP request to {} with status code {}".format(URL, response.status_code))

def get_month():
    x = datetime.datetime.now()
    month = int(x.strftime("%m"))
    return month