from sys import stdin
n = int(stdin.readline())
for i in range(n):
    A = int(input())
    cout = 0
    lis = list(map(int,input().split()))[:A]
    lis.sort()
    for j in range(0,A):
        m = 0
        p = 0
        for k in range(0,A):
            if lis[j]>=lis[k]:
                m = m +1
            elif lis[j]<lis[k]:
                p = p +1
        if m>p:
            cout = cout + 1
    print(cout)
                    
                
    