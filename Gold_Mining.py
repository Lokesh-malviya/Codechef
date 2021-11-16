n = int(input())
for i in range(n):
    A,B,C = map(int,input().split())
    A = A+1
    mul = A*C
    if mul>=B:
        print("YES")
    else:
        print("NO")
    