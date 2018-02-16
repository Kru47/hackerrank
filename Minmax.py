def miniMaxSum(arr):
    arr.sort()
    min=0
    max=0
    for i in range(4):
        min += arr[i]
    for i in range(len(arr)-1,len(arr)-5,-1):
        max += arr[i]
    return min,max



arr = list(map(int, input().strip().split(' ')))
res=miniMaxSum(arr)
print(" ".join(map(str,res)))