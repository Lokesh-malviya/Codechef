n = int(input())
for i in range(n):
    A,B,C = map(int,input().split())
    Run = 2*C + A
    if Run>=B:
        print("YES")
    else:
        print("NO")