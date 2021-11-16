text = input()
c = 0
for i in text:
    if i!=' ':
        c = c + 1
word = list(text.split(' '))
print(c/len(word))