dwarves = [int(input()) for i in range(9)]

total = sum(dwarves)
break_point = False
#ex) 1, 3 난쟁이가 빼야되는 난장이야
#x =1 j = 3 일 때 -> 답이 나왔지? if 걸렸지?
#if문 -> 1, 3 난쟁이를 제외하지? -> 골랐으니까 for 문은 끝나야하지?
#
for x in range(len(dwarves)-1):
    if break_point:
        break
    for j in range(x+1,len(dwarves)):
        if 100 == (total - (dwarves[j] + dwarves[x])):
            num1 = dwarves[x] 
            num2 = dwarves[j]

            dwarves.remove(num1)
            dwarves.remove(num2)
            dwarves.sort()
            break_point = True
            break
print(dwarves)