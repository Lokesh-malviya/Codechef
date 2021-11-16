n = int(input())
for i in range(n):
    for j in range(23): 
        if i!=4:
            if i==0 or i==n-2:
                if j!=0 and j<6:
                    print("x",end="")
                else:
                    print(" ",end="")
            elif i==1 or i==n-3:
                if j%6==0:
                    print("x",end="")
                else:
                    print(" ",end="")
            elif i==2:
                if j!=6 and j%6==0:
                    print("x",end="")
                else:
                    print(" ",end="")
            elif i==3:
                if j==0:
                    print("x",end="")
                elif (j>9 and j<15) or (j>15 and j<21):
                    print("x",end="")
                else:
                    print(" ",end="")
        else  :
                if j!=6 and j%6==0:
                    print("x",end="")
                else:
                    print(" ",end="")
               
    print()