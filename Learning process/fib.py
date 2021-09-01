#use appending
fib = [1,1]

print(fib)
for i in range (2, 101):
    nextElement = fib[i-1] + fib[i-2]
    fib.append(nextElement)
print(fib[10])

#use recursion
def fib(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fib(x-1) + fib(x-2)    
print(fib(10))    