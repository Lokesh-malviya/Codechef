n = int(input())
for i in range(n):
        N,X = map(int,input().split())
        A = list(map(int,input().split()))[:N]
        D = []
        count = 0
        dict1 = {}
        for j in range(N):
            G = A[j]
            for k in range(N):
                if j!=k:
                    print(A[j],X)
                    F = A[k]^X
                    print(F)
                    if G == F:
                        count = count + 1
                        dict1[G]=count
            count = 0
        S = list(dict1.values())
        
        