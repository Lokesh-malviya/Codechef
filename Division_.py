from functools import reduce
n = int(input())
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
for i in range(n):
    A,B,C = map(int,input().split())
    fact = factors(A)
    lis = list(fact)
    lis.sort()
    i = 0
    p = []
    while A!=1:
        A=A/lis[i]
        if i<len(lis):
            p.append(lis[i])
            fact = factors(A)
            lis = list(fact)
            lis.sort()
        i = i + 1
    print(p)