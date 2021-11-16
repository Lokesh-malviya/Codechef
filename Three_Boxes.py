n = int(input())
for i in range(n):
    A,B,C,D = map(int,input().split())
    sum = A+B+C
    rem = sum//D
    if rem>=1 and rem<=2 :
        print((sum%D)+1)
    else:
        print(3)