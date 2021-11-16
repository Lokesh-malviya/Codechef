from sys import stdin
n = int(stdin.readline())
for i in range(n):
    X,Y = map(int,input().split())
    if X%2==0 :
        if X==0 and Y%2!=0:
            print("NO")
        else:
            print("YES")
    else:
        print("NO")