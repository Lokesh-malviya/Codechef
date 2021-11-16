from sys import stdin, stdout

n = int(stdin.readline())
for i in range(n):
    P = int(input())
    A = input()
    count = 0
    D = A.split('0')
    C = A.split('1')
    D.remove('')
    print(D)
