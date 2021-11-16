from sys import stdin,stdout
n = int(stdin.readline())
for i in range(n):
    A,B = map(int,input().split())
    if A<B:
        mins = abs(B-A)
        rem = mins/2
        if rem.is_integer():
            print(int(rem))
        else:
            print(int(rem+1.5))
    elif A>B:
        print(int(abs(B-A)))
    else:
        print(0)