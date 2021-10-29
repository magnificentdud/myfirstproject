N, M = map(int, input().split())
board = list()
for i in range(N):
    board.append(input())
repair = list()

for i in range(N-7):
    for j in range(M-7):
        first_w = 0
        first_b = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y)%2 ==0:
                    if board[x][y] != 'w':
                        first_w = first_w+1
                    if board[x][y] != 'b':
                        first_b = first_b+1
                else:
                    if board[x][y] != 'b':
                        first_w = first_w+1
                    if board[x][y]!= 'w':
                        first_b = first_b+1
        repair.append(first_b)
        repair.append(first_w)
print(min(repair))