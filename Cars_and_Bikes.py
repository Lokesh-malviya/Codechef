from sys import stdin, stdout
n = int(stdin.readline())
for j in range(n):
    A = int(stdin.readline())
    h = A%4
    if h>=2:
        print("YES")
    else:
        print("NO")
    