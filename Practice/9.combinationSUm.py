# Python3 program to find out all
# combinations of positive
# numbers that add upto given number

# arr - array to store the combination
# index - next LOCATION in array
# num - given number
# reducedNum - reduced number
def findCombinationsUtil(arr, index, num,
                         reducedNum):
    # Base condition
    if (reducedNum < 0):
        return;

        # If combination is
    # found, print it
    if (reducedNum == 0):

        for i in range(index):
            print(arr[i], end=" ");
        print("");
        return;

        # Find the previous number stored in arr[].
    # It helps in maintaining increasing order
    prev = 1 if (index == 0) else arr[index - 1];

    # note loop starts from previous
    # number i.e. at array LOCATION
    # index - 1
    for k in range(prev, num + 1):
        # next element of array is k
        arr[index] = k;

        # call recursively with
        # reduced number
        findCombinationsUtil(arr, index + 1, num,
                             reducedNum - k);


def findCombinations(n):
    # array to store the combinations
    # It can contain max n elements
    arr = [0] * n;
    #print(arr)

    # find all combinations
    findCombinationsUtil(arr, 0, n, n);


# Driver code
n = 7;
findCombinations(n);