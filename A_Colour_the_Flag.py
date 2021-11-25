n = int(input())
for i in range(n):
    A,X = map(int,input().split())
    lis = []
    for i in range(A):
        pis = []
        A = input()
        lis.append(A)
    for j in lis:
        st = str(j)
        S = st.count('R')
        R =  st.count('W')
        if S>0 and R>0:
            p = st.index('R')
            q = st.index('W')
            if p%2!=0 and q%2==0:
                for k in range(len(j)):
                     if k%2==0:
                         if j[k]=='.':
                             j[k] == 'W'
                     else:
                          if j[k]=='.':
                                 j[k] == 'R'
            if p%2==0 and q%2!=0:
        if S>0 and R==0:
            p = st.index('R')
            if p%2!=0:
                for k in range(len(j)):
                     if k%2==0:
                         if j[k]=='.':
                             j[k] == 'W'
                     else:
                          if j[k]=='.':
                                 j[k] == 'R'

                             