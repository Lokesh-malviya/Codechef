n = int(input())
for i in range(n):
    A,B,C = map(int,input().split())
    lis = list(map(int,input().split()))[:A]
    st = sum(lis[0:B])
    st1 = sum(lis[:])
    if st==B:
        if st1==A:
            print(100)
        else:
            print(C)
    else:
        print(0)