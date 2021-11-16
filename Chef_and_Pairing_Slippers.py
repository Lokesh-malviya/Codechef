from sys import stdin
n = int(stdin.readline())
for i in range(n):
    A,B,C = map(int,input().split())
    if A!=B:
        minus = A-B
        if minus<B:
            print(minus*C)
        elif minus>=B:
            print(B*C)
    else:
        print(0)