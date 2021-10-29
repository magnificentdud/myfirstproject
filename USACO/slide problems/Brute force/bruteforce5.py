from itertools import permutations

n = int(input())
o = ['+','-','*','/']
num = list(map(int, input().split()))
op = list(map(int, input().split()))
oper = []

for i in range(4):
    for k in range(op[i]):
        oper.append(o[i])

oper = list(set(permutations(oper, len(oper))))
print(oper)

ans = []

for i in oper:
    n = num[0]
    for j in range(len(num)):
        if i[j]=='+':
            n += num[j+1]
        elif i[j]=='-':
            n -= num(j+1)
        elif i[j]=='*':
            n *= num[j+1]
        else:
            if n//num[j+1]<0:
                n = -(-n//num[j+1])
            else:
                n = n//num[j+1]
    ans.append(n)

print(max(ans), min(ans))