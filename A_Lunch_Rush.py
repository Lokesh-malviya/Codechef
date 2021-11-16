n,k = map(int,input().split())
lst = []
for i in range(n):
    B,C = map(int,input().split())
    if C<k:
        lst.append(B)
    elif C>=k:
        G = B - (C-k)
        lst.append(G)
print(max(lst))
        
        