n = int(input())
for i in range(n):
    A,B,C = map(int,input().split())
    S = input()
    V = S.count("0")
    F = S.count("1")
    print(B*V + C*F)