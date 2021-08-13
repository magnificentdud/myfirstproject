x = input().upper()
keys = list(set(x))  

cnt_list = []
for y in keys :
    cnt = x.count(y)
    cnt_list.append(cnt)  

if cnt_list.count(max(cnt_list)) > 1 :  
    print('error')
else :
    max_index = cnt_list.index(max(cnt_list))  

    print(keys[max_index])