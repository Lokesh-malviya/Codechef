from sys import stdin, stdout
n = int(stdin.readline())
for j in range(n):
    A = int(stdin.readline())
    F = str(stdin.readline())
    sum = 0
    for i in range(A):
        sum = sum + int(F[i])
    D = F.count('0')
    R = F[0:A-1]
    H = R.count('0')
    Rdx = len(R)-H
    print(sum + Rdx)