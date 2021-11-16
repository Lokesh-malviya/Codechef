n = int(input())
for i in range(n):
    A,B,C = map(int,input().split())
    Sum = A-B
    P = B*3
    Q = Sum*(-1)
    De = P+Q
    if De>=C:
        print("PASS")
    else:
        print("FAIL")