n = int(input())
lst = []
count = 0
sount = 0
for i in range(n):
    B,C = map(int,input().split())
    if B>C:
        count = count + 1
    elif B<C:
        sount = sount + 1
if count >=1 and sount>=1:
    print("Happy Alex")
else:
    print("Poor Alex")
