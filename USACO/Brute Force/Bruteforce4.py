n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(input()))

check = min(m,n)
ans = 0
for i in range(n):
    for j in range(m):
        for d in range(check):
            if ((i+d) < n) and ((j+d) < m) and (arr[i][j] == arr[i][j+d] == arr[i+d][j] == arr[i+d][j+d]):
                ans = max(ans, (d+1)**2)

print(ans)