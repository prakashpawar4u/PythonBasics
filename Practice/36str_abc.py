import pdb
str1 = 'abcdefgh'
n = 3
output = ""
for i in range(0,len(str1),n):
    str2 = (str1[i:i+n])

    if len(str2) >= 3:
        str3 = (str2[::-1])
        output = output + " " + str3
    else:
        output = output + " " + str2

print("Final Output of the string is :", output)

"""
n=3
out=""
for i in range(0,len(str1),n):
    pdb.set_trace()
    str2=str1[i:i+n]
    if len(str2)>=3:
        str3=str2[:: -1]
        #str3=''.join(reversed(str2))
        out=out+str3
    else:
        #str3=''.join(str2)
        #str
        out = out+str2
    print (str3)
print(out)


for i in `ps -eaf | grep -i iperf | grep -i {} | awk {}`;
    do sudo kill -9 $i;
    done
"""