n = int(input())
for i in range(n):
    A,B,C,D,E = map(int,input().split())
    lst = [A+B,B+C,A+C]
    if lst[0]<=D and C<=E:
        print("YES")
    elif lst[1]<=D and A<=E:
        print("YES")
    elif lst[2]<=D and B<=E:
        print("YES")
    else:
        print("NO")
        