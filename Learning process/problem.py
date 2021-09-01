n = int(input())
my_list = list(map(int, input().split()))
max = my_list[0]
min = my_list[0]

for i in my_list:
    if i > max:
        max = i
    if i < min:
        min = i
print(min, max)
