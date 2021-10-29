number = int(input())
cnt = 0
for i in range(1, number//3):
    for j in range(1, number//3):
        for k in range(1, number//3):
            sum_num = 3*(i+j+k)
            if sum_num == number:
                cnt += 1
print(cnt)

