n = int(input())
for i in range(n):
    A = int(input())
    S = input()
    j = S.count('RR')
    p = S.count('LL')
    if   j>0 or p>0:
        print("YES")
    else:
        print("NO")  