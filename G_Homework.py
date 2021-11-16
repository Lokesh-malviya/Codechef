dict1 = {}
S= input()
n = int(input())
for i in range(len(S)):
    dict1[S[i]]=S.count(S[i])
print(dict1)