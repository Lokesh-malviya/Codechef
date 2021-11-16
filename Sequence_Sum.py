from sys import stdin, stdout

n = int(input())
for j in range(n):
    A = int(stdin.readline())
    sn = (A*(22 + (A-1)*6)//2)%1000000007
    stdout.write(str(sn) + "\n")
