from sys import stdin, stdout
def calculate(max1,max2):
    sum1 = max1*3
    sum2 = max2*1
    print(sum1-sum2)
n = int(stdin.readline())
for i in range(n):
    A = int(stdin.readline())
    if A%2!=0:
        max1 = (A//2)+1
        max2 = A//2
        calculate(max1,max2)
    else:
        max1 = A//2
        max2 = max1
        calculate(max1,max2)