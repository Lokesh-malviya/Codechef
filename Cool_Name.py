from sys import stdin, stdout

def calculate(A):
    sum = 0
    for i in range(len(A)):
        sum = sum + (i+1)*(ord(A[i])-96)
    print(sum)
n = int(stdin.readline())
for i in range(n):
    A = list(map(str,input()))
    A.sort()
    calculate(A)