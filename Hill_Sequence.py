from sys import stdin
n = int(stdin.readline())
for i in range(n):
    A = int(input())
    lis = list(map(int,input().split()))[:A]
    lil = []
    pil = []
    flag = 0
    max1 = max(lis)
    lis.sort()
    dict1 = {}
    for j in lis:
        if lis.count(j)>2 or lis.count(max1)==2:
            flag = 1
            break
        dict1[j] = lis.count(j)
    i = 0
    if flag==1:
        print(-1)
    else:
        for k in dict1:
            if dict1[k]==1:
                lil.append(k)
            else:
                lil.insert(i,k)
                pil.append(k)
            i = i+1
        gym =lil+pil
        gym.reverse()
        print(*gym)
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
    """if lis.count(lis[j])>2 or lis.count(max1)==2:
            flag = 1
            break
        if lis[j] == lis[j+1]:
            kp = lis[j]
            lis.remove(kp)
            
            lis.insert(A-1,kp)  
    if flag==1:
        print(-1)
    else:
        lis.reverse()
        print(*lis)"""
    """else:
        D = set(lis)
        K = set(lil)
        pis = list(D)
        jis = list(K)
        pri = pis+jis
        pri.reverse()
        print(*pri)"""
        
    