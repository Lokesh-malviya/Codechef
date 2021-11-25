import math
n = int(input())
for i in range(n):
    A = int(input())
    lis = list(map(int,input().split()))[:A]
    gc = lis[0]
    pis = []
    for i in lis:
        gc = math.gcd(gc,i)
        pis.append(gc)
    if lis==pis:
        print(*pis)
    else:
        print(-1)

    
    
    