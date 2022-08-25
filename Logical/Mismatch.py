st1 = "aaaaatnac"
st2 = st1[::-1]

print(st2)

cnt = 0
for i in range(len(st1)):
    if st1[i]==st2[i]:
        print("number matching")
    else:
        cnt+=1
print("The number of mismatches are {}".format(cnt))

