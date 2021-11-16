words = ["aaaa","asas","able","ability","actt","actor","access"]
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
flag = 0
kis = []
for i in puzzles:
            ki = []
            lis = []
            sum1 = i[0]
            
            for j in i:
                lis.append(j)
            for item in words:
                pis = []
                if item.count(sum1)>0:
                    the = item
                    for items in item:
                        
                        pis.append(items)
                    p = set(pis)
                    d = set(lis)
                    if p.issubset(d)==True:
                        ki.append(the)
                else:
                    continue
            f = set(ki)
            dim = len(f)
            if dim > 0:
                kis.append(dim)
            else:
                kis.append(0)
print(*kis)
                
                            
            