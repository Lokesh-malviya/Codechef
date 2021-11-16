n = int(input())
lst = list(map(int,input().strip().split()))[:n]
f = int(n%3)
G = 3-f
for i in range(G):
    lst.append(0)
H = int(len(lst)//3)
k = 0
l = 1
m = 2
lst2 = []
lst1 = []
lst3 = []
for j in range(H):
    lst1.append(lst[k])
    lst2.append(lst[l])
    lst3.append(lst[m])
    k = k + 3
    l = l + 3
    m = m + 3
B = sum(lst1)
P = sum(lst2)
Q = sum(lst3)
cst = [B,P,Q]
X = max(cst)
U = cst.index(X)
if U==0:
    print("chest")
elif U==1:
    print("biceps")
elif U==2:
    print("back")