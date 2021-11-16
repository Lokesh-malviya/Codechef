n = int(input())
for i in range(n):
    lis = list(map(int,input().split()))
    A = lis.count(1)
    B = lis.count(2)
    if A>B:
        print("INDIA")
    elif A==B:
        print("DRAW")
    else:
        print("ENGLAND")