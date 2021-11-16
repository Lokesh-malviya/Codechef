n = int(input())
for i in range(n):
        N = int(input())
        A = list(map(int,input().split()))[:N]
        lst = []
        pst = []
        count = 0
        sount = 0
        for g in range(N):
            if A[g]%2==0:
                lst.append(A[g])
                count = count + 1
            else:
                pst.append(A[g])
                sount = sount + 1
        m = 0
        k = 1
        sum = 0
        for j in range(1,N+1):
            if j%2!=0 and m<len(pst):
                lst.insert(j,pst[m])
                m = m + 1  
            if count>0 :
                S = k + lst[j-1]
                k = k + 1
                I = S%2
                sum = sum + I
            elif count>0 and sount==0:
                sum = int(N//2)+1
            elif count == 0 and sount >0:
                sum = int(N//2)
            
        print(sum)
            
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
        