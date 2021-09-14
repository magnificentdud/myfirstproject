N , M = map(int, input().split())

arr = list(map(int, input().split()))
result = 0
for i in range(N):
    for j in range(i+1, N):
        for f in range(j+1, N):
            if arr[i] + arr[j] + arr[f] > M:
                continue
            else:
                result = max(result, arr[i] + arr[j] + arr[f])
print(result)