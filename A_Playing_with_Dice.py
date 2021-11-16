n,m = map(int,input().split())
count = 0
sount = 0
Dount = 0 
for i in range(1,7):
    G = abs(n-i)
    H = abs(m-i)
    if G<H:
        count = count + 1
    elif H<G:
        sount = sount + 1
    else : 
        Dount = Dount + 1
if n>m or m>n:
    print(count,Dount,sount)
else:
    print(count,Dount,sount)
        
