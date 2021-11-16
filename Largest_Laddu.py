from sys import stdin, stdout
import math
n = int(stdin.readline())
for i in range(n):
    A = int(input())
    p = 2**A
    lis = list(map(int,input().split()))[:p]
    if A>0:
        lis.sort()
        len1 = p//2
        sum1 = sum(lis[0:len1])
        sum2 = sum(lis[len1:])
        if abs(sum1-sum2)<=1:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")