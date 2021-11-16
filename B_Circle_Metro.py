n,a,x,b,y = map(int,input().split())
F = a
lst = []
pst = []
E = b
count = 0
for j in range(1,n+1):
    
    if F>n:
        F = x
    if F == x:
        lst.append(F)
        break
    lst.append(F)
    F = F+1
    
for k in range(1,n+1):
    if E<1:
        E = y
    if E == y:
        pst.append(E)
        break
    pst.append(E)
    E = E-1
if len(lst)>len(pst):
      for l in range(len(pst)):
        if lst[l]==pst[l]:
            count = 1
            break
        else:
            continue
else:
    for l in range(len(lst)):
        
        if lst[l]==pst[l]:
            count = 1
            break
        else:
            continue
print(lst,pst)
if count == 1:
    print("YES")
else:
    print("NO")