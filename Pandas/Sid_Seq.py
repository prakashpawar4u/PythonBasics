import pandas as pd
from pandas import ExcelWriter

# st = """9843011210;1210;9843011211;1211;9843011212;1212;9843011213;1213;st4.admin.lab;35891705-211210-1;35891705-211211-1;35891705-211212-1;35891705-211213-1;2;RCS11-TMO-AUTO.st4.admin.lab;10.10.197.166
# sip:mavodi-0-4a-12-1-ffffffff-12@scscf.st4.admin.lab:5070;sip:mavodi-0-4a-f-2-ffffffff-f:5070"""

l1 = ['9843011210', '1210', '9843011211', '1211', '9843011212', '1212', '9843011213', '1213', 'st4.admin.lab', '35891705-211210-1', '35891705-211211-1', '35891705-211212-1', '35891705-211213-1', '2', 'RCS11-TMO-AUTO.st4.admin.lab']
l2 = ['10.10.197.166\nsip:mavodi-0-4a-12-1-ffffffff-12@scscf.st4.admin.lab:5070', 'sip:mavodi-0-4a-f-2-ffffffff-f:5070']
summary_data = l1 + l2
#summary_data = [summary_data]]
writer = "sequential.xlsx"
df = pd.DataFrame([summary_data])
df.to_excel(writer, sheet_name='Summary')