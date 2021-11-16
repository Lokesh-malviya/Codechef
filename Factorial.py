import sys
sys.setrecursionlimit(24000)
n = int(input())
"""def factorial1(A):
    if A==1:
        return 1
    else:
        return A*factorial1(A-1)"""
def factorial1(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact
for i in range(n):
    A = int(input())
    j = factorial1(A)
    s = str(j)
    S = s[::-1]
    count = 0
    
    for j in S:
        if j!='0':
            break
        else:
            count = count + 1
    print(count)