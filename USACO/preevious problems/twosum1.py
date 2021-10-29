nums = list(map(int, input().split()))
target = int(input())

for i in range(len(nums)):
    for j in range(len(nums)):
        if i == j:
            continue
        if nums[i]+nums[j]== target:
            print(i,j)