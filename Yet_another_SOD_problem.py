n = int(input())
for i in range(n):
    A,B = map(int,input().split())
    Y = (B-A)/3
    h = str(Y)
    for j in range(len(h)):
        if h[j]=='.':
            R = int(h[j+1])
            break
    if R>3:
        print(int(Y)+1)
    else:
        print(int(Y))