n,m = map(int,input().split())
pst = []
for i in range(n):
    lst = list(map(int,input().strip().split()))
    for j in range(lst[0]):
        if lst[j+1]<m:
            pst.append(lst[0])
        break


pst.sort()
print(len(pst))
for item in pst:
    print(item,end=" ")