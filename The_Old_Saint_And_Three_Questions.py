n = int(input())
for i in range(n):
    A1,A2,A3 = map(int,input().split())
    B1,B2,B3 = map(int,input().split())
    sum = A1+A2+A3
    dum = B1+B2+B3
    if sum == dum:
        print("Pass")
    else:
        print("Fail")