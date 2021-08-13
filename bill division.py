n, k = map(int,input("n,k:").split())
bill = list(map(int,input("bill:").split()))
b = int(input("b: "))

#calculation
A = (sum(bill)-bill[k])/2
if b > A:
    print(b-A)
else:
    print("bon appetit")

