n = int(input())
for i in range(n):
    A = int(input())
    S = input()
    A = S.count('U')
    B = S.count('D')
    if A>0 and B==0:
        F = S.replace('U','D')
    elif A==0 and B>0:
        F = S.replace('D','U')
    elif A==0 and B==0:
        F = S
    elif A>0 and B>0:
        T = S.replace('U','O')
        W = T.replace('D','U')
        F = W.replace('O','D')          
    print(F)