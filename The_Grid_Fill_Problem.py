n = int(input())
for i in range(n):
    A =int(input())
    if A%2==0:
        for i in range(A):
            for j in range(A):
                print("-1",end=" ")
            print()
    else:
        for i in range(A):
            for j in range(A):
                if i==j:
                    print("-1",end=" ")
                else:
                    print("1",end=" ")
            print()