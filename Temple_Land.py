from sys import stdin, stdout
n = int(stdin.readline())
for j in range(n):
    A = int(stdin.readline())
    arr = [int(x) for x in stdin.readline().split()]
    count = 0
    if A%2==0:
        print("no")
    else:
        for j in range(0,A//2):
            if arr[j]==j+1:
                if arr[j]==arr[A-j-1]:
                    count = 1
                else:
                    count = 0
            else:
                count = 0
        if count == 1:
            print("yes")
        else:
            print("no")
    