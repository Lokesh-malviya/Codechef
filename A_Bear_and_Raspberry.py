n,k = map(int,input().split())
lst = list(map(int,input().strip().split()))[:n]
lst1 = []
for i in range(n-1):
    A = lst[i]-lst[i+1]
    lst1.append(A)
J = max(lst1)
if (J>=1) and (J>k):
    print(J-k)
else:
    print(0)