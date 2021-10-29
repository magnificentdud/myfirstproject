n = int(input)
arr = list(map(int, input().split()))
group = 0

odd = 0
even = 0

for i in arr:
    if i% 2 == 0:
        even+=1
    if i%2 == 1:
        odd += 1
#print(even, odd)    

#짝수가 더 많을 때
if even > odd:
    group = odd*2
    even_s = even-odd
    group += 1
#홀수가 더 많을 때
elif even < odd:
    group = even*2
    odd_s = odd - even
    odd_mod = [2,-1,1]
    group += (odd_s//3) * 2 + odd_mod[odd_s%3] 
#짝수 홀수가 같을 때
else:
    group = even*2


print(group)
