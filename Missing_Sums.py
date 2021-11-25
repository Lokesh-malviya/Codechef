n = int(input())
for i in range(n):
    A = int(input())
    lis = []
    for j in range(1,2*A+1):
        if j%2!=0:
            lis.append(j)
    print(*lis)
    