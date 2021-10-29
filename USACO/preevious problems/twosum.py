nums = list(map(int, input().split()))
target = int(input())


for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] + nums[j] == target:
            if nums[i]==nums[j]:
                continue
           
            print(i,j)              