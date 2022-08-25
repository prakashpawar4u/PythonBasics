val =  "python"

# length = len(val)
#
# for i in range(0,length):
#     val = val[1:length] + val[0]
#     print(val)

s = "python"
for i in s:
	print (s[s.index(i):]+s[:s.index(i)])

print(s.index("n"))
