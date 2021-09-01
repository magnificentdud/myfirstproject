cnt = int(input())
x = int(input())
arr = list(map(int, input().split()))
for i in range(cnt):
    if arr[i] < x:
        print("i%d arr[i]:%d x:%d"%(i,arr[i],x))
        print(arr[i], end=" ")