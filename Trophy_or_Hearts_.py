n = int(input())
for i in range(n):
    A = input()
    B = input()
    R = A.lower()
    G = B.lower()
    set1 = set(R)
    set2 = set(G)
    count = 0
    for j in set1:
        for k in set2:
            if j==k:
               count = count + 1
    print(count) 
    
