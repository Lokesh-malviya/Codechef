from sys import stdin, stdout
from itertools import permutations
import math
n = int(stdin.readline())
def find_gcd(x, y):
     
    while(y):
        x, y = y, x % y
     
    return x
         
 

for j in range(n):
    A = int(stdin.readline())
    lst = []
    U = []
    for i in range(1,A+1):
        lst.append(i)
    pst = list(permutations(lst,4))
    for k in range(len(pst)):
        for h in range(1,A+1):
            U.append(pst[k][h-1]+h)
 
        num1 = U[0]
        num2 = U[1]
        gcd = find_gcd(num1, num2)
        for i in range(2, len(U)):
            gcd = find_gcd(gcd, U[i])
        if gcd>1:
            for g in U:
                print(g,end=" ") 
    