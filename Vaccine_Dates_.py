n = int(input())
for i in range(n):
    D,L,R = map(int,input().split())
    if D>=L and D<=R:
        print("Take second dose now")
    elif D>R:
        print("Too Late")
    else:
        print("Too Early")
