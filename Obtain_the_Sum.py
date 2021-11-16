n = int(input())
for i in range(n):
    A,B = map(int,input().split())
    Sum = A*(A+1)//2
    W = Sum - B
    if W<=A and W>=1:
        print(W)
    else:
        print(-1)
    