n = int(input())
for i in range(n):
    A = int(input())
    lis = list(map(int,input().split()))[:A]
    pis = lis
    pis.sort()
    print(pis)
    p = 0
    m = []
    k = 0
    for j in range(A):
        if pis[j]>p:
            o = lis.index(pis[j],j)
            lis.remove()
    