num_cards, max_sum = map(int, input().split())

card_nums = list(map(int, input().split()))

p_value = 0

for i in card_nums:
    for j in card_nums:
        for k in card_nums:
            
            sum = i+j+k
            if sum > max_sum or i==j or j==k or i==k:
                continue
            
            if sum > p_value:
                p_value = sum
print(p_value) 