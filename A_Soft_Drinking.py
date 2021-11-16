n, k, l, c, d, p, nl, np = map(int,input().split())
H = k*l/nl
D = c*d
T = p/np
lst = [H,D,T]
print(int(min(lst)/n))