n = int(input())
lst = list(map(int,input().strip().split()))[:n]
pst = list(map(int,input().strip().split()))[:n+1]
U = sum(lst)
Y = sum(pst)
print(Y-U)