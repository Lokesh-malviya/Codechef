n = int(input())
for i in range(n):
    p = int(input())
    g = p%4
    if g==0 :
            print("North")
    elif g==1:
            print("East")
    elif g==2:
            print("South")
    elif g==3:
            print("West")
   