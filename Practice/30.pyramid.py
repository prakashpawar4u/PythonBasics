# def pypart(n):
#     #outer loop
#     for i in range(0,n):
#         #inner loop
#         for j in range(0,i+1):
#             print("* ",end= "")
#         print("\r")
#
# if __name__ == "__main__":
#     n= 5
#     pypart(n)
#####################################################
# def pypart(n):
#     mylist = []
#     for i in range(1,n+1):
#         mylist.append("*"*i)
#     print(mylist)
#     print('\n'.join(mylist))
#
# n=5
# pypart(n)
#####################################################
#
# def leftTriangle(n):
#     k = 2*n - 2
#     #outer loop to handle num of rows
#     for i in range(0,n):
#
#         #inner loop to handle number of spaces
#         for j in range(0,k):
#             print(end=" ")
#         k = k -2
#         for j in range(0,i+1):
#             print("* ", end="")
#         print("\r")
# n=5
# leftTriangle(n)


#####################################################
# def Triangle(n):
#     k = 2*n -2
#
#     for i in range(0,n):
#         for j in range(0,k):
#             print(end=" ")
#
#         k = k -1
#         for j in range(0, i+1):
#             print("* ",end="")
#         print("\r")
# n = 5
# Triangle(n)

#####################################################
# def numpat(n):
#     num = 1
#     for i in range(0,n):
#         #num = 1
#         for j in range(0,i+1):
#             print(num, end=" ")
#             num = num + 1
#         print("\r")
# n = 5
# numpat(n)

#####################################################
def charpat(n):
    num = 65
    for i in range(0,n):
        #num = 1
        for j in range(0,i+1):
            print(chr(num), end=" ")
            num = num + 1
        print("\r")
n = 5
charpat(n)
