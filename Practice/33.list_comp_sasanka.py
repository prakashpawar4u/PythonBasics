inp = ["1, Jack, jill", "2, james, anderson"]

#out = [[ 1, "Jack", "Jill"], [2, "james", "anderson"]]

#[[1, ' Jack', ' jill'], [2, ' james', ' anderson']]
# out = [[int(x.split(',')[0])] + x.split(',')[1:] for x in inp]
# print(out)

fout = []
for i in inp:
    out=i.split(',')
    fout.append(out)
print(fout)