from sys import stdin, stdout
n = int(stdin.readline())
for i in range(n):
    s = input()
    W = s.count('1')
    D = s.count('0')
    if W>D:
        print("YES")
    else:
        print("NO")