"""import math
n = int(input())
print(2,3,5,7,end=" ")
for i in range(2,n+1):
    if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
        if math.ceil(math.sqrt(i)) != math.floor(math.sqrt(i)):
            print(i,end=" ")"""
import sympy
n = int(input())
for i in range(1,n+1):
    if sympy.isprime(i)==True:
        print(i,end=" ")