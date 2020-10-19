from bottle import route, run, template
import os

@route('/')
def index():
    try:
        port=8000
        command='''kill -9 $(netstat -nlp | grep :'''+str(port)+''' | awk '{print $7}' | awk -F"/" '{ print $1 }')'''
        os.system(command) 
        os.system("nohup python /www/wwwroot/api-soft3888.ddns.net/scripts/backend.py &")
        os.system('\n echo "Backend up"')
    except Exception:
        pass

run(host='localhost', port=9999)