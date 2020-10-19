import time
import database
from event import Event

all_data=database.get_data()
events={}
for data in all_data:
    temp=Event(data[0],data[1],data[2])
    events[temp.get_start()]=temp
# print(events)

while True:
    time_now = time.strftime("%H:%M", time.localtime())
    if time_now in events.keys():
        events[time_now].do_action()
        time.sleep(61)