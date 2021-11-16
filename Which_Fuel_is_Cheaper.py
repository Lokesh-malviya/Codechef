from sys import stdin
n = int(stdin.readline())
for i in range(n):
    X,Y,A,B,K = map(int,input().split())
    s1 = A*K
    S2 = B*K
    sum1 = X+s1
    sum2 = Y+S2
    if sum1>sum2:
        print("DIESEL")
    elif sum1<sum2:
        print("PETROL")
    else:
        print("SAME PRICE")