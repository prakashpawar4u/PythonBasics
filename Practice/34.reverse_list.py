#Reverse a string
# st = "this is to reverse a list"
# st_list = st.split()
# rev_st = st_list[::-1]
# print(type(rev_st))
# print(" ".join(rev_st))


l = [1,2,3,4,5]
rev = l[::-1]

print("Reversed:", rev)
for i in range(1,len(l) + 1):
    print(i , l[-i])
    #print(i, l[-int(i)+1])


