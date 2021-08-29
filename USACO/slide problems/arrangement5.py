num = int(input())
score_list = list(map(int , input().split()))
max_score = max(score_list)

for i in range(num):
    score_list[i] = score_list[i] / max_score * 100

print(sum(score_list)/num)


