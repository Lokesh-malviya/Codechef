from sys import stdin, stdout
n = int(stdin.readline())
for i in range(n):
    A = int(input())
    S = A-1
    if A!=3:
        for j in range(0,A):
            for k in range(0,A):
                if j!=A-3 and j!=A-2 and j!=A-1:
                    if k==S:
                        print("Q",end="")
                        S = S-1
                    else:
                        print(".",end="")
                elif j==A-3:
                    print(".",end="")
                elif j==A-2:
                    if k!=1:
                        print(".",end="")
                    else:
                        print("Q",end="")
                elif j==A-1:
                    print(".",end="")
            print()
    else:
        print("...\n.Q.\n...")
                    
            
