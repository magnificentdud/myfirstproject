#making factorial function
x = int(input())
def factorial(x):
    if x == 1 or 0:
        return 1
    else:
        return x * factorial(x-1)
print(factorial(x))