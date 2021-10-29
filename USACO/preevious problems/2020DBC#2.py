n = int(input())
list0 = list(map(int, input().split()))
answer = 0


for i in range(len(list0)):
    for j in range(i,len(list0)):
        flower_count  = j - i +1
        sum_patal = 0
        avg = 0
        for k in range(i,(i+flower_count)):
            sum_patal += list0[k]
        if sum_patal % flower_count != 0:
            continue
        avg = sum_patal//flower_count
        tmp = list0[i:j+1]
        if avg in tmp:
            answer += 1

print(answer)
