temperatures = [89,62,70,58,47,47,46,76,100,70]
flag = 0
sum = 0
j = 0
lis = []
for i in range(len(temperatures)):
    sum = 0
    for j in range(i+1,len(temperatures)):
        if temperatures[j]> temperatures[i]:
            sum1 = i
            sum2 = j
            sum = sum2 - sum1
            
            break
    
    lis.append(sum)
print(lis)
    


        

            
         