n = int(input())
for i in range(n):
    N = int(input())
    lis  = list(range(1,N+2))
    if N>2:
        K = lis[N]-lis[0]
        lst1 = [str(lis[0]),str(K)]
        P = lis[N]-lis[1]
        lst2 = [str(lis[1]),str(P)]
        print("YES")
        print(" ".join(lst1))
        print(" ".join(lst2))
    else:
        print("NO")
    