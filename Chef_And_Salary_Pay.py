from sys import stdin,stdout
n = int(stdin.readline())
for i in range(n):
    A,B = map(int,input().split())
    cou = 1
    S = input()
    P = S.count('1')
    lis = list(S.split('0'))
    gis = []
    pis = []
    for j in lis:
        D = len(j)
        pis.append(D)
    
    Jan = set(pis)
    max1 = max(Jan)
    sum = max1*B + P*A
    stdout.write(str(sum)+"\n")