i, j, k = map(int, input().split())
array = list(map(int, input().split()))

n = array[i-1:j]
n.sort()
print(n[k-1])


