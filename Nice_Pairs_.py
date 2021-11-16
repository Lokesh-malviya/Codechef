from sys import stdin,stdout
n = int(input())
for i in range(n):
    p = int(stdin.readline())
    for line in stdin:
        A = line
    count = 0
    for j in range(len(A)):
        for K in range(j+1,len(A)):
            p = K-j
            sum = abs(int(A[K])-int(A[j]))
            if sum == p:
                count = count +1
    stdout.write(str(count)+"\n")