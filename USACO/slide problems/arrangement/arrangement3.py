a = int(input())
b = int(input())
c = int(input())
value = a*b*c
value = str(value)
for num in range(10):
    print(value.count(str(num)))