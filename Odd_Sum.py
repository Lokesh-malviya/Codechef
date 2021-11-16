from sys import stdin,stdout
n = int(stdin.readline())
for i in range(n):
    A = int(stdin.readline())-1
    sum = A*(A+1)/2
    stdout.write((str(int(sum))+"\n"))