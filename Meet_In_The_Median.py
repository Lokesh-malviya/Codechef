from itertools import combinations
n = int(input())
for i in range(n):
    A,B = map(int,input().split())
    lst = list(map(int,input().strip().split()))[:A]
    Cst = list(combinations(lst,B))
    temp = 0
    Ed = []
    for j in range(len(Cst)):
        Ad = list(Cst[j])
        Ps = Ad.copy()
        Ad.sort()
        if B%2!=0:
            R = int(B//2)
            F = Ad[R]
            if F>temp:
                temp = Ad[R]
                Ed = Ps.copy()
        else:
            R = int(B//2)-1
            F = Ad[R]
            if F>temp:
                temp = Ad[R]
                Ed = Ps.copy()
    print(Ad[R])
    for item in Ed:
        print(item,end=" ")