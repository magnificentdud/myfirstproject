x = int(input())


def fibo(n):
    if n<= 1 or n ==0:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))
for i in range(1,x+1):
        print(fibo(i))

zero = [1, 0, 1]
one = [0, 1, 1]

def fibonacci(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print('{} {}'.format(zero[num], one[num]))

T = int(input())
    
for _ in range(T):
    fibonacci(int(input()))
