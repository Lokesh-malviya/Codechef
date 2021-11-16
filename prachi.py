n = int(input())
print("Print the american flag")
print("----------------------")
for i in range(n):
    for j in range(45):
        if i%2==0:
            if j%2==0 and j<=12:
                print("*",end="")
            elif j%2!=0 and j<=12:
                print(" ",end="")
            else:
                print("=",end="")
        else:
            if j%2!=0 and j<=12:
                print("*",end="")
            elif j%2==0 and j<=12:
                print(" ",end="")
            else:
                print("=",end="")
    print()