a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
x = input()
for y in a:
    x = x.replace(y,'*')
print(len(x))
