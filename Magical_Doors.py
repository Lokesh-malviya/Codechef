from sys import stdin, stdout
n = int(stdin.readline())
for i in range(n):
    N = stdin.readline()
    P= N
    count = 0
    for j in range(len(P)):
        if P[j] =='0':
            P = P.replace('0','W')
            P = P.replace('1','0')
            P = P.replace('W','1')
            count = count + 1
        else:
            continue
    print(count)