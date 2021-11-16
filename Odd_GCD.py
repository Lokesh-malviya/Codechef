n = int(input())
for i in range(n):
    A = int(input())
    lis= list(map(int,input().split()))[:A]
    pst = []
    for j in lis:
        if j%2==0:
            pst.append(j)
    J = min(pst)
    while J%2!=0:
        j = j//2
        count = count + 1
    
    