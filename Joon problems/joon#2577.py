# a = int(input())
# b = int(input())
# c = int(input())
# value = a*b*c
# value = str(value)
# for num in range(10):
#     print(value.count(str(num)))


A = int(input())
B = int(input())
C = int(input())

v = A*B*C
count = [0] * 10

v = str(v)


for i in v:
    i = int(i)
    count[i] += 1
for i in count:
    print(i)
    