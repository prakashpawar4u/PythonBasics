import matplotlib.pyplot as plt
import csv
import pandas as pd

SINR = ['17.6', '27.2', '26.6', '25.0', '25.0', '24.0', '23.2', '22.0', '20.8', '20.4', '19.4', '18.4', '16.2', '15.6', '14.8', '12.6', '12.4', '12.8', '11.0', '10.0']
RSRP = ['-105', '-95', '-96', '-97', '-98', '-99', '-100', '-101', '-102', '-103', '-104', '-105', '-107', '-108', '-109', '-110', '-111', '-112', '-113', '-114']
DLTP = [147.0, 147.0, 147.0, 147.0, 147.0, 144.0,145.0, 147.0,147.0, 147.0, 147.0, 147.0, 147.0, 147.0, 144.0, 147.0, 136.0, 127.0, 147.0, 147.0]

sinr = [float(x) for x in SINR]
rsrp = [float(y) for y in RSRP]
dl_tp = [float(z) for z in DLTP]

print(len(sinr),sinr)
print(len(rsrp),rsrp)
print(len(dl_tp),dl_tp)

df = pd.DataFrame({'rsrp':rsrp,'sinr':sinr})
#print(df)
df.to_csv('Input.csv')


df2 = pd.read_csv("Input.csv")
print("DF2",df2)
l1_rsrp = df2["rsrp"]
print(l1_rsrp,type(l1_rsrp))



