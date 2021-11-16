import math
n = int(input())
for i in range(n):
    A,B = map(int,input().split())
    k = str(A)
    if str(A).count(str(B))>0:
        if A%10!=0:
            A = str(A)
            no = int(A[0:2])+1
            p = len(A)-2
            last = str(no)+p*'0'
            print(int(last)-int(A))
        else:
            if k.count('0')==len(str(A))-1:
                A = str(A)
                p = len(str(A))-1
                no = int(p*'1')
                print(no)
            else:
                A = str(A)
                no = int(A[0:2])+1
                p = len(A)-2
                last = str(no)+p*'0'
                print(int(last)-int(A))
    else:
        print(0)
        
        
    