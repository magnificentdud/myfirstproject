list0 = list(map(int, input().split()))

list0.sort()
A = list0[0]
B = list0[1]
C = list0[-1]-A-B

print(A,B,C)