# possib_v = []
# for k in range(10):
#     mush_p = int(input())

#     possib_v.append(mush_p)
# final_v = []


# for i in range(11):
#     p_v = list(sum(possib_v[1:i]))
# for k in p_v:
#     final_v.append(p_v-100)
#     final_v.sort
# print(final_v)

m = []
score = 0
for i in range(10):
    m.append(int(input()))
for j in m:
    score += j
    if score > 100:
        if score-100 > 100 - score + j:
            score -= j
        break
print(score)

