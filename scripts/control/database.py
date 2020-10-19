import sys
sys.path.append('/etc/openhab2/scripts/control')
import sqlite3
import util
import json

def connect():
    config = util.read_config()
    conn = sqlite3.connect(config['SETTING']['database'])
    return conn

def reader(event):
    connection=connect()
    cursor = connection.cursor()
    command='''SELECT time_slot from timing where event="{}";'''.format(event)
    cursor.execute(command)
    res=cursor.fetchone()[0]
    return res

def get_data():
    result = []
    connection=connect()
    cursor = connection.cursor()
    command='''SELECT time_slot,event,actions from timing ORDER BY id ASC;'''
    cursor.execute(command)
    res=cursor.fetchall()
    a = [a[1] for a in res]
    b = [b[0] for b in res]
    c = [c[2] for c in res]
    result=list(zip(a, b, c))
    return result

def update_data(event_time_list):
    connection=connect()
    cursor = connection.cursor()
    for key in event_time_list.keys():
        if "-" not in key:
            command='''UPDATE timing SET time_slot="{}" WHERE event="{}";'''.format(event_time_list[key],key)
            cursor.execute(command)
        else:
            print(key,event_time_list[key])
    cursor.close()
    connection.commit()