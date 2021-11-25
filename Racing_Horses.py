sim = capacity
step = 0
j = 0
lis = []
for i in plants:
    if i<=capacity:
        capacity = capacity - i
        step = step + 1
    else:
        capacity = sim
        capacity = capacity - i
        step = step + j + (j+1)
    j = j + 1   
return(step)

    