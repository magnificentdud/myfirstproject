input #enter가 눌러지기 전까지 입력 받는거야
n = int(input())

m,n,k,v = map(int,input().split())
print(m,n,k,v)
print(type(n))


#리스트
a = []
b = list(map(int,input().split()))
print(b)

#2차원 리스트
n = int(input())
for _ in range(n):
    a = list(map(int,input().split()))