n = int(input())
lst = list(map(int,input().strip().split()))[:n]
pst = lst.copy()
lst1 = []
lst2 = []
lst3 = []
for i in range(1,n-1):
   pst.remove(lst[i])
   lst1.append(pst)
   pst = lst.copy()
for j in range(len(lst1)):
    F = len(lst1[j])
    for t in range(F-1,0,-1):
        H = lst1[j][t]-lst1[j][t-1]
        lst2.append(H)
    
    A = max(lst2)
    lst3.append(A)
    lst2 = []

print(min(lst3))
    
        