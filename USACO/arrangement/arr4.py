# A = int(input())
# B = int(input())
# C = int(input())
# D = int(input())
# E = int(input())
# F = int(input())
# G = int(input())
# H = int(input())
# I = int(input())
# J = int(input())

# a = []

# a.append(A%42)
# a.append(B%42)
# a.append(C%42)
# a.append(D%42)
# a.append(E%42)
# a.append(F%42)
# a.append(G%42)
# a.append(H%42)
# a.append(I%42)
# a.append(J%42)

# a = set(a)
# print(len(a))


a = []

for i in range(10):
    n = int(input())
    a.append(n%42)
a = set(a)
print(len(a))