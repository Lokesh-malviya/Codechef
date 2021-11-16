n = int(input())
for i in range(n):
    N,K,L =  map(int,input().split())
    lst = list(map(int,input().strip().split()))
    S = max(lst[0:N-1])
    O = lst[N-1]
    count = 0
    if O<S:
        if K>0:
            O = O + K*(L-1)
        elif K<0:
            print("No")
            break
        if S<O:
            print("Yes")
        elif O==S:
            print("No")  
    else:
        print("No")
    
    

    
    