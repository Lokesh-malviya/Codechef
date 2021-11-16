n = int(input())
for i in range(n):
    p,a,b,c,x,y = map(int,input().split())
    sum = p//a
    if sum>=x*b:
        dum = sum - x*b
        if dum > y*c:
            print(x+y)
        else:
            print(x)
    else:
        print(0)