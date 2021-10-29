nums = list(map(int, input().split()))

m = nums[0]


for i in range(0, len(nums)):
    for j in range(i, len(nums)):
        s = sum(nums[i:j+1])
        if s > m:
            m = s
print(m)


        
