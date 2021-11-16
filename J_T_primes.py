n = int(input())
lst = list(map(int,input().strip().split()))[:n]
pst = []
for i in range(n):
    for j in range(1,lst[i]+1):
        if lst[i]%j==0:
            pst.append(j)
        Dst = set(pst)
        F = list(Dst)
    if len(pst)==3:
        print("YES")
    else:
        print("NO")
    pst = []