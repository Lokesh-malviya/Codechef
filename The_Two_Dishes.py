n = int(input())
for i in range(n):
    A,B = map(int,input().split())
    Y = A-B
    F = A-abs(Y)
    print(F)
    