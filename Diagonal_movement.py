n = int(input())
for i in range(n):
    A,B = map(int,input().split())
    H = abs(A)
    J = abs(B)
    sum = H+J
    if sum%2==0:
        print("YES")
    else:
        print("NO")