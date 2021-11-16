from sys import stdin
n = int(stdin.readline())
for i in range(n):
    A,B = map(int,input().split())
    sum = 2*A
    rem = A*B-1
    print(int(sum),int(rem*B*A))
    