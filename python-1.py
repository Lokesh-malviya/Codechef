# program A

"""len1 = float(input())
bred = float(input())
print(int(len1*bred))"""

#program B
"""X1,Y1 = map(int,input("Enter he value of X1 and Y1 : \t").split())
X2,Y2 = map(int,input("Enter he value of X2 and Y2 : \t").split())
print(f"answer : {abs(X1-X2)+abs(Y1-Y2)}")
"""

#program C
name = input("Enter the name of student : \t")
maths,english,science = map(int,input("Enter the tyhe marks in 3 subject : \t").split())
print("******************Score card*******************")
print(f"Name : {name}")
print("******************Marks*******************")
print(f"Maths : {maths} \n English : {english} \n Science : {science}")
print("***************Total marks****************")
print(f"Tortal marks : {maths+english+science}")
print(f"percentage is : {((maths+english+science)/300)*100} %")
print("***************Total marks****************")
print(f"After the increment you percentage is {(((maths+english+science)/300)*100)+.5}")
