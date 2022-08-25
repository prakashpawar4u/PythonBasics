import csv
l1 = ['9843011210', '1210', '9843011211', '1211', '9843011212', '1212', '9843011213', '1213', 'st4.admin.lab', '35891705-211210-1', '35891705-211211-1', '35891705-211212-1', '35891705-211213-1', '2', 'RCS11-TMO-AUTO.st4.admin.lab']
l2 = ['10.10.197.166\nsip:mavodi-0-4a-12-1-ffffffff-12@scscf.st4.admin.lab:5070', 'sip:mavodi-0-4a-f-2-ffffffff-f:5070']
#
summary_data = l1 + l2
#splitter = i.split("\n")

#writer = ExcelWriter(r"C:\Users\pawarp\PycharmProjects\LearnPytest\Refactored_Py_DS_ML_Bootcamp-master\myexcel.xlsx")


csv1 = "sequential.csv"
csv1 = open(csv1,"w+")
l3 = []
for i in summary_data:
    #print(len(i),i)
    splitter = i.split("\n")
    l3.append(splitter)

writer = csv.writer(csv1)
l3 = l3
header = [str(x) for x in range(0,18)]
header = [header]
print("L3",l3,len(l3))
print("Header:", header, len(header))

writer.writerows(header)
writer.writerows(l3)