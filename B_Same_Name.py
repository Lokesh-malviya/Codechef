n = int(input())
lst = []
lst1 = []
for i in range(n):
    n,t = map(str,input().split())
    lst = [n,t]
    lst1.append(lst)
count = 0
sount = 0
for j in range(len(lst1)-1):
    for k in range(j+1,len(lst1)):
        if lst1[j][0] == lst1[k][0] and lst1[j][1]==lst1[k][1]:
            count = count + 1
            break
    break
            
if count>=1:
    print('Yes')
else:
    print('No')