# def check_palindrome(mystr):
#     st = mystr
#     rev_st = st[::-1]
#     for i in range(len(st)):
#         if st[i]==rev_st[i]:
#             print(st[i],rev_st[i])
#             print("both are matching")
#         else:
#             print("Both are not matching")
#             return 0
#     return 1
#
# mystr = "madam"
# isPalindrome = check_palindrome(mystr)
# if isPalindrome:
#     print("Can be rearranged to make a palindrome")
# else:
#     print("Cannot be a palindrome")


def check_palindrome(s):
    return s == s[::-1]
s = "malayalam"
ans = check_palindrome(s)

if ans:
    print("its a palindrome")
else:
    print("No, str cannot be a palindrome")



##############################################