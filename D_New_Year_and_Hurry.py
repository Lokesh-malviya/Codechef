N,A = map(int,input().split())
S = 5
lst = []
count = 0
sum = 0
J = 240-A
for i in range(1,N+1):
    sum = sum + 5*i
    if sum > J:
        break;
    count = count + 1
print(count)
 