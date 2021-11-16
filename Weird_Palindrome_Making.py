from sys import stdin
n = int(stdin.readline())
for i in range(n):
    A = int(input())
    lis = list(map(int,input().split()))[:A]
    count = 0
    for j in range(A):
        if lis[j]%2!=0:
            count = count + 1
    print(count//2)