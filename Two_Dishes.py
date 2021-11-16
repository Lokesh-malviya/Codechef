n = int(input())
for i in range(n):
    N,A,B,C = map(int,input().split())
    if A<=B:
        sum = A
        p = B-A
        if p>=C:
            dum = C
        else:
            dum = p
    else:
        sum = B
        p = A-B
        if p>=C:
                dum = C
        else:
            dum = p
    gym = sum + dum
    if gym>=N:
        print("YES")
    else:
        print("NO")