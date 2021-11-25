import math
n = int(input())
for i in range(n):
    A,B = map(int,input().split())
    lis = []
    pis = []
    for i in range(A):
        sum = 0
        S = input()
        lis.append(S)
        for j in range(0,len(S)):
            if S[j]=='1':
                sum = sum + j+1
        pis.append(sum)
    for k in range(A):
        for l in range(k+1,A):
            temp = 
    