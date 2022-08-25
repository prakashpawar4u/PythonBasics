import os
import re
import pandas as pd
from datetime import datetime

def conVertEpoc(t):
    epoch_t = t
    time_stamp = pd.to_datetime(epoch_t, unit='s')
    print(time_stamp.tz_localize('UTC').tz_convert('Europe/Berlin'))
    #print(type(time_stamp.tz_localize('UTC').tz_convert('Europe/Berlin')))
    euroTime = str(time_stamp.tz_localize('UTC').tz_convert('Europe/Berlin')).split(".")[0].split(" ")[1]
    print("MY Conveterd time :", euroTime, type(euroTime))
    return euroTime

def LatAverage(num):
    try:
        sum_num = 0
        for t in num:
            sum_num = sum_num + float(t)
        avg = sum_num / len(num)
        avg = "%.2f" % avg
        return avg
    except Exception as e:
        pass

def readPingStat(fp):
    fp= open(fp, 'r')
    pingData = fp.readlines()
    pingData = pingData[1:]
    lenOfFile = len(pingData)
    i = 0

    avgLat = []
    nd= {}
    #for i in range(0, lenOfFile, 5):
    for i in range(0, 100, 5):
        print("Iteration: ",i)
        j = i+5
        sublist = pingData[i:j]
        latList = []
        for k in sublist:
            pat = "\[(\d+\.\d+)\]\s+.*\=(\d+\.\d+)"
            if re.search(pat, k):
                match = re.search(pat, k)
                print("Epoch Time:{} RTT: {}".format(match.group(1), match.group(2)))
                latList.append(match.group(2))
        i = i + i
        print("Converting Epoch time")
        EuropeTime = conVertEpoc(match.group(1))
        avgLatency =LatAverage(latList)
        avgLat.append([EuropeTime, avgLatency])
        print("Average latency:",len(avgLat))

        pd.DataFrame(avgLat).to_csv("Modified.csv")

        #break

if __name__=="__main__":
    fp = r"C:\Users\pawarp\PycharmProjects\LearnPytest\preparation\\interview\\SidDtag\\ping.txt"
    readPingStat(fp)
