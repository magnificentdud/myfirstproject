n = int(input())
position = []
for i in range(n):
    N, M = list(map(int, input().split()))
    position.append([N, M])
print(position)
ans = []
for a in range(n):
    for b in range(n):
        for c in range(n):
            
            if a==b or b==c or c==a:
                continue
           
            if position[a][0]==position[b][0] and position[a][1]==position[c][1]:
                A = abs(position[a][1]-position[b][1])*abs(position[a][0]-position[c][0])
                ans.append(A)
print(ans)
print(max(ans))