a = int(input())
b=0
for i in range(2,a):
    if a%i==0:
        b = 1
if b == 0:
        print("prime number")
else:
    print("not a prime number")
