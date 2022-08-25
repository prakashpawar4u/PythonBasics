def get_minima(l,s):
    new_l = []
    minima_l = []

    for i in range(0, len(l), s):
        print(l[i:i+s])
        new_l.append(l[i:i+s])
        minima_l.append(min(l[i:i+s]))
    return new_l, minima_l

#l = list(range(25))
l = [2,3,4,5,5,6,7,8,83,4,5,6,7,84,6,34,23,556,6,5,33,4,55,3]
s = 3

new_l, minima_l = get_minima(l,s)

print(new_l)
print(minima_l)