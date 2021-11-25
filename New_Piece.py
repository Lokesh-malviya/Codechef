n = int(input())
for i in range(n):
    A,X,Y,Z = map(int,input().split())
    sum1 = A+X
    sum2 = Y+Z
    if A==Y and X==Z:
        print(0)
    elif (sum1%2==0 and sum2%2==0) or (sum1%2!=0 and sum2%2!=0) :
        print(2)
    else:
        print(1)