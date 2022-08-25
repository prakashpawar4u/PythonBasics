
def countSwaps(arr):
    # Write your code here
    pass
    print(a)
    n = len(arr)
    for i in range(n):
        swapped = False
        #5-0-1
        #5-1-1
        #5-2-1
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        print("Iteration {} : {}".format(i,arr))
        if swapped== False:
            break
    print("Arr:", arr)

if __name__== '__main__':
    n = int(input().strip())
    print("N", n)
    a = list(map(int, input().rstrip().split()))
    #print(a)
    countSwaps(a)