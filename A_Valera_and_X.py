n = int(input())
lst1 = []
J = ""
H = 0
D = 0
for i in range(n):
    S = input()
    lst1.append(S)
    J = J + S
for j in range(n):
    for k in range(n):
        if j==k:
            
            if lst1[j][k]==J[0] :
                H = H + 1
            if lst1[j][n-k-1]==J[0]:
                D = D+1
Q = J.count(J[1])
if (H+D) == 2*n:
    if Q == (n*n - (2*n-1)) :
        print("YES") 
    else:
        print("NO")
else:
    print("NO")