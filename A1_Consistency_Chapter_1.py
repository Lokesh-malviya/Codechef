n = int(input())
for i in range(n):
    A = input()
    lst = []
    lst1 = []
    dict1 = {}
    dict2 = {}
    M = i+1
    if len(A)>1:
        for h in A:
            if h == 'A' or h=='E' or h=='I' or h=='O' or h=='U': 
                lst.append(h)
                dict1[h]=A.count(h)
            else:
                lst1.append(h)
                dict2[h]=A.count(h)
        print(len(lst),len(lst1))
        X = len(lst)
        Y = len(lst1)
        if X>Y:
            pst = list(dict2.values())
            if len(pst)>0:
                J = len(lst1)-max(pst)
            else:
                J = 0
            Ds = len(lst)+2*J
            print(f'Case #{M}:',Ds)
        elif X<Y:
            pst = list(dict1.values())
            if len(pst)>0:
                J = len(lst)-max(pst)
            else:
                J = 0
            Ds = len(lst1)+2*J
            print(f'Case #{M}:',Ds)
        else:
            se1 = set(lst)
            se2 = set(lst1)
            if len(se1)<len(se2):
                pst = list(dict1.values())
                if len(pst)>0:
                    J = len(lst)-max(pst)
                else:
                    J = 0 
                Ds = len(lst)+2*J
                print(f'Case #{M}:',Ds)
            elif len(se1)>len(se2):
                pst = list(dict2.values())
                if len(pst)>0:
                    J = len(lst1)-max(pst)
                else:
                    J = 0 
                Ds = len(lst)+2*J
                print(f'Case #{M}:',Ds)   
    else:
        print(f'Case #{M}:',0)