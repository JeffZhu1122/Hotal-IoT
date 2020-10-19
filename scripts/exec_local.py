from bottle import route, run, template,redirect,request
import os
import sys
sys.path.append('/etc/openhab2/scripts/control')
import database
import util
import json

@route('/exec')
def exec():
    try:
        config=util.read_config()
        path=config['SETTING']['root_path']
        os.system('''ps -ef | grep {}/ | cut -c 9-15 | xargs kill -9'''.format(path)) 
        os.system("setsid python3 "+path+"/{} &".format(config['SETTING']['include']))
        os.system('\n echo "system_run,py up"')
        # files=os.listdir(path)
        # exclude=config['SETTING']['exclude'].split(",")
        # for f in files:
        #     if f in exclude:
        #         continue
        #     else:
        #         os.system("setsid python3 "+path+"/"+f+" &")
        #         os.system('\n echo "{} up"'.format(f))
    except Exception:
        pass

@route('/')
def index():
    return redirect("/admin")

@route('/admin',method='GET')
def admin():
    name=[]
    time=[]
    action=[]
    all_data=database.get_data()

    for data in all_data:
        name.append(data[0])
        time.append(data[1])
        actions=json.loads(data[2])
        temp_list=[]
        for key in actions:
            temp={}
            temp[key]=actions[key]
            temp_list.append(temp)
        action.append(temp_list)
    return template("admin",time=time, name=name, action=action)

    
@route('/admin',method='POST')
def do_admin():
    database.update_data(request.forms)
    return redirect("/admin")

run(host='0.0.0.0', port=9999)