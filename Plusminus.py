
import sys

def plusMinus(arr,n):
    pos = 0
    neg = 0
    zer = 0
    for i in range(n):
        if arr[i] > 0:
            pos += 1
        if arr[i] < 0:
            neg += 1
        if arr[i] == 0:
            zer += 1
    print('{0:.6f}'.format(float(pos/n)))
    print('{0:.6f}'.format(float(neg / n)))
    print('{0:.6f}'.format(float(zer / n)))

n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
print(arr)
plusMinus(arr, n)