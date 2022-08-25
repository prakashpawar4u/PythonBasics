def swap_position(li, p1, p2):
    li[p1], li[p2] = li[p2], li[p1]
    return li

l = ['11', '22', '33', '44', '55', '66', '77']
print("Before List : ", l)
p1, p2 = 2, 5

l2 = swap_position(l, p1,p2)
print("After List : ", l2)





