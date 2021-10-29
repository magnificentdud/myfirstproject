n = int(input())

c = []
#이 함수의 목적은? num가 소수인지 아닌지?? True or False
def prime(n):
    #j 2 ~ (num-1) 이사에는 num로 나누어서 떨어지는 수가 없어야지
    for j in range(2,n):
        # 2~num-1 사이에서 나누어 떨어지는 수가 하나라도 있는 경우 
        if n%j == 0:
            return False
    return True
count = 0

for i in range(n, 2*n+1):
    if prime(i):
        c.append(i)
        count += 1
print(len(c))