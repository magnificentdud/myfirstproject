numbers = set()
for i in range(10):
    x = int(input())
numbers.add(x%42)
print(len(numbers))