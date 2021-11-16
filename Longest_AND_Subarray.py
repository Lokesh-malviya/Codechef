import math
n = int(input())
for i in range(n):
    A = int(input())
    count = 2
    i = 1
    lis = []
    if A>2:
        loc  = int(math.log(A,2))
        sum = int(math.pow(2,loc))
        D = A-sum+1
        I = sum//2
        if D>I:
            print(D)
        else:
            print(I)
    else:
        print(1)
    