c_a = input()

s = input() 

count = 0 
answer = 0

while (count != len(s)):
    answer += 1
    for i in c_a:
        if i == s[count]:
            count += 1
        if count == len(s):
            break        
    
print(answer)