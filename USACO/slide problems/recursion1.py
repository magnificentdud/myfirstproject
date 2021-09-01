x = int(input())


def fibo(n):
    if n<= 1 or n ==0:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))
print(fibo(x))

    



























# a = int(input())
# zero = [1,0,1]
# one = [0,1,1]

# def calculate(num):
#     length = len(zero)
#     if length<= num:
#         for i in range(length, num+1):
#             zero.append(zero[i-1]+zero[i-2])
#             one.append(one[i-1]+one[i-2])
#             print(zero)
#             print(one)
#     print("%d %d"%(zero[num],one[num]))

# for i in range(a):
#     k = int(input("put an integer  "))
#     calculate(k)
