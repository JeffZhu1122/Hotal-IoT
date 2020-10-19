import time
import database
from event import Event

all_data=database.get_data()
events=[]
for data in all_data:
    temp=Event(data[0],data[1],data[2])
    temp1={}
    events.append({temp.get_s})