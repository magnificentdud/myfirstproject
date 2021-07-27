fib = [0,1]

print(fib)
for i in range (2, 101):
    nextElement = fib[i-1] + fib[i-2]
    fib.append(nextElement)
print(fib)
