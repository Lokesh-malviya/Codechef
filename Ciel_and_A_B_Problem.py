A,B= map(int,input().split())
minus = A-B
j = str(minus)
if j[len(j)-1] == '9':
    print(minus-1)
else:
    print(minus+1)