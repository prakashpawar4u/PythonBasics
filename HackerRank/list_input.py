
# if __name__ == '__main__':
#     # N = int(input())
#     #     # print("Entered Numbe is :", N)
#     my_list = []
#     #     # actionList = []
#     #     # for i in range(N):
#     #     #     k = input("Enter the action")
#     #     #     actionList.append(k)
#     #     # print("Action List", actionList)
#     actionList = ['insert 0 5', 'insert 1 10', 'insert 0 6', 'print ', 'remove 6']
#     for j in actionList:
#         y = j.split(" ")
#         my_list.eval(y[0])(y[1], y[2])
#     print(my_list)


arr = []
for i in range(int(input())):
    s = input().split()
    for i in range(1, len(s)):
        s[i] = int(s[i])

    if s[0] == "append":
        arr.append(s[1])
    elif s[0] == "extend":
        arr.extend(s[1:])
    elif s[0] == "insert":
        arr.insert(s[1], s[2])
    elif s[0] == "remove":
        arr.remove(s[1])
    elif s[0] == "pop":
        arr.pop()
    elif s[0] == "index":
        print(arr.index(s[1]))
    elif s[0] == "count":
        print(arr.count(s[1]))
    elif s[0] == "sort":
        arr.sort()
    elif s[0] == "reverse":
        arr.reverse()
    elif s[0] == "print":
        print(arr)