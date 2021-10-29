# x = list(map(int, input()))
# print(x)
# for i in range(len(x)):
#     if x[i]==x[-1-i]:
#         print('true')
#     else:
#         print('false')


a = input()
b = []
c = []
for i in a:
    b.append(i)
for j in range(len(b)): 
    c.append(b[-(j+1)])
if b == c:
    print('true')
else:
    print('false')