n = int(input())
for i in range(n):
    A = input()
    count = 0
    for j in A:
        if j=='0' or j=='1' or j=='3' or j=='8':
            count = 1
        else:
            count = 0
            break
    if count == 1:
        print("LOVELY")
    else:
        print("NOT LOVELY")