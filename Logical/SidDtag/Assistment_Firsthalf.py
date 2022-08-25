#from contextlib import AbstractAsyncContextManager
#import os
import re
#from this import d
import pandas as pd
#from datetime import datetime

def conVertEpoc(t):
    #This function is use to convert Epoch time to Europe/Berlin timestamp.
    epoch_t = t
    time_stamp = pd.to_datetime(epoch_t, unit='s')
    print(time_stamp.tz_localize('UTC').tz_convert('Europe/Berlin'))
    euroTime = str(time_stamp.tz_localize('UTC').tz_convert('Europe/Berlin')).split(".")[0].split(" ")[1]
    print("MY Conveterd time :", euroTime, type(euroTime))
    return euroTime

def LatAverage(num):
    #This function takes list of 5 Rtt value and takes the average of those 5 values and return as Float value with 2 floating values.
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

        print("Average latency Length:",len(avgLat))
        print("Average latency:",avgLat)
        colName = ["Time", "Latency"]
        df1=pd.DataFrame(avgLat, columns = colName)


        #df1 = pd.DataFrame(df1, columns=colName)
        #df1.columns = list("AB")

        pd.DataFrame(df1).to_csv("Modified_Ping.csv", index=False)

def AddLatency():
    df2 = pd.read_csv(
        r'C:\\Users\pawarp\PycharmProjects\LearnPytest\preparation\\interview\\SidDtag\\NetworkLog.csv', sep=';',
        engine='python')
    df2 = df2[['Date', 'Time', 'GlobalCellId']]
    df2["Time"] = df2["Time"].str.replace("(\.+\d+)", "")

    df1 = pd.read_csv(
        r'C:\\Users\pawarp\PycharmProjects\LearnPytest\preparation\\interview\\SidDtag\\Modified_Ping.csv', sep=',',
        engine='python')

    print("#~" * 30)
    df_common = df1.loc[df1['Time'].isin(df2['Time'])]
    #print(df_common)

    newDF = pd.merge(df2, df_common, on=['Time'])
    print(newDF.head())
    pd.DataFrame(newDF).to_csv("FinalLatency.csv", index=False)

if __name__=="__main__":
    #fp = "c:\\Users\\sandis\\AppData\\Local\\Programs\\Python\\Python39\\sidharth\\chapter1\\ping.txt"
    fp = r"C:\Users\pawarp\PycharmProjects\LearnPytest\preparation\\interview\\SidDtag\\ping.txt"
    readPingStat(fp)
    AddLatency()

