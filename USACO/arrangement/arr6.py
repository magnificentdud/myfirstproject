dials = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
time = 0
word = input()
for k in range(len(word)):
    for i in dials:
        if word[k] in i:
            time+=dials.index(i)+3
print(time)

