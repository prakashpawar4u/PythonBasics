import pandas as pd
from pandas import ExcelWriter


st = """9843011210;1210;9843011211;1211;9843011212;1212;9843011213;1213;st4.admin.lab;35891705-211210-1;35891705-211211-1;35891705-211212-1;35891705-211213-1;2;RCS11-TMO-AUTO.st4.admin.lab;10.10.197.166
sip:mavodi-0-4a-12-1-ffffffff-12@scscf.st4.admin.lab:5070;sip:mavodi-0-4a-f-2-ffffffff-f:5070"""
writer = "sequential.xlsx"
l1 = ['9843011210', '1210', '9843011211', '1211', '9843011212', '1212', '9843011213', '1213', 'st4.admin.lab', '35891705-211210-1', '35891705-211211-1', '35891705-211212-1', '35891705-211213-1', '2', 'RCS11-TMO-AUTO.st4.admin.lab']
l2 = ['10.10.197.166\nsip:mavodi-0-4a-12-1-ffffffff-12@scscf.st4.admin.lab:5070', 'sip:mavodi-0-4a-f-2-ffffffff-f:5070']

summary_data = l1 + l2
sum_col = [str(x) for x in range(0,17)]

# print(pd.Series(data=summary_data,index=sum_col))

print(summary_data)
df = pd.DataFrame([summary_data])
print(df)
df.to_excel(writer, sheet_name='Summary')
df.to_csv("Sidd.csv", index=False)