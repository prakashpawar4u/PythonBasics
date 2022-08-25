def anagram(st1, st2):
    n1 = len(st1)
    n2 = len(st2)

    #if length of both strings is not same then it cannot be a anagram:
    if n1 != n2:
        print("Strings lengths are different!!!!!")
        return 0

    st1 = sorted(st1)
    st2 = sorted(st2)

    #compare two sorted strings
    for i in range(0,n1):
        if st1[i] != st2[i]:
            return 0
    return 1

st1 = "silent"
st2 = "listen"

if anagram(st1, st2):
    print("The two strings are anagram of each other")
else:
    print("The two strings are not anagram of each other")
