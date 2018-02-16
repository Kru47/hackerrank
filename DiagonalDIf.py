#!/bin/python3

import sys

def diagonalDifference(a,n):
     sumx = 0
     sumy = 0
     for i in range(n):
          sumx = sumx + a[i][i]
     for j in range(n):
          sumy = sumy + a[n - j - 1][j]
     return abs(sumx-sumy)

n = int(input().strip())
a = []

for a_i in range(n):
     a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
     a.append(a_t)

result = diagonalDifference(a,n)
print(result)
