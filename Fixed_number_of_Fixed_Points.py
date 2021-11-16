n = int(input())
for i in range(n):
    A,B = map(int,input().split())
    lis = list(range(1,A+1))
    diff = B-A
    if abs(diff)!=1:
        J = lis[A-1]
        lis.insert(B,J)
        print(*lis[0:A])
    else:
        print(-1)
        