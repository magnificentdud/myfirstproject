arr=[[11,2,4],[4,5,6],[10,8,-12]]

for i in range(3):
    for j in range(3):
        print(arr[i][j],end="")
    print("")
x = len(arr)
d1 = sum([arr[i][i] for i in range(x)])
d2 = sum([arr[i][x-1-i] for i in range(x)])

if d1 > d2:
    print(d1-d2)
elif d2>d1:
    print(d2-d1)
else:
    print(0)