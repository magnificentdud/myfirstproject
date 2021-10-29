nums = list(map(int, input().split()))
prime = []
for i in range(len(nums)-2):
    for j in range(i+1, len(nums)-1):
        for k in range(j+1, len(nums)):
            a = nums[i]+nums[j]+nums[k]
            for f in range(2, a):
                if a%f != 0:
                    prime.append(f)
                else:
                    del f
print(len(prime))