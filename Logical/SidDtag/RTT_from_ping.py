import os
import re
from datetime import datetime

#newfilename = "C:/Users/eanasxx/Desktop/pythonji/Tsystems/ping.txt"
newfilename = "C:/Users/pawarp/PycharmProjects/MyGit/prakashpawar4u/python/Logical/RTT/ping.txt"
n=open(newfilename,'r')
for i in n:
    #print(i)
    if(i[0]=='['):
        str=i[1:18]
        #print(str)   
        ptr=float(str)
        rtt=i[74:]
        print(datetime.utcfromtimestamp(ptr).strftime('%H:%M:%S.%f'),rtt)
    
