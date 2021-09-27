dials = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
a = input()
sol = 0
for k in range(len(a)):
    for i in dials:
        for a[k] in i:
            sol += dials.index(i)+3
print(sol)

