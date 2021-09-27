from itertools import permutations

n = int(input())
o = ['+','-','*','/']
num = list(map(int, input().split()))
op = list(map(int, input().split()))
oper = []

for i in range(4):
    for k in range(op[i]):
        oper.append(o[i])

oper = (set(permutations(oper, len(oper))))
print(oper)