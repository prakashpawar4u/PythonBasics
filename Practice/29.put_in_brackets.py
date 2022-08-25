st = "Hi There, How Are You doing, I said Hi"
#(H)i (T)here, (H)ow (A)re (Y)ou doing, (I) said (H)i
l = st.split(" ")
#['Hi', 'There,', 'How', 'Are', 'You', 'Doing,', 'I', 'said', 'Hi']
newl = []
for i in l:
    #print(i[0], i[1:])
    if i[0].isupper():
        newl.append("({}){}".format(i[0],i[1:]))
    else:
        newl.append(i)
print(newl)
#newstr = ""

print(" ".join(newl))
    #print(type(i))
    #newl.append("({})".format(i[0]))
