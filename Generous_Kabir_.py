n = int(input())
for i in range(n):
    A,B = map(int,input().split())
    lis = list(map(int,input().split()))[:A]
    count = 0
    for J in lis:
        if J>=B:
            count = count + 1
    print(count)