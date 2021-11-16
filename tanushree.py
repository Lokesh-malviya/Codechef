
def divisible(i,m):
    if i%m==0:
        return i
    else:
        return 0

n,m = map(int,input().split())
lst = []
for i in range(1,n+1):
    SP = divisible(i,m)
    lst.append(SP)
for j in lst:
    if j!=0:
        print(j,end=" ")