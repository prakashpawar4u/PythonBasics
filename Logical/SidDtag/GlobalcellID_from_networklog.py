import re
import csv
pat = "(\d+\:\d+\:\d+\.\d+).*LTE\;(\d+)"
#file = "C:/Users/eanasxx/Desktop/pythonji/Tsystems/NetworkLog.csv"
file = "C:/Users/pawarp/PycharmProjects/MyGit/prakashpawar4u/python/Logical/RTT/NetworkLog.csv"
with open(file, 'r', encoding='utf-8') as csv_file:
#with open(file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = []
    for i in csv_reader:
        rows.append(i[0])
    for j in rows:
        if re.search(pat,j):
            match = re.search(pat, j)
            print(match.group(1),match.group(2))
            
        
            

