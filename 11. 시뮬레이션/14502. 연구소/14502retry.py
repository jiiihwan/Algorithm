import sys
from collections import deque
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

empty = []
virus = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            empty.append((i,j))
        elif board[i][j] == 2:
            virus.append((i,j))

def bfs():
    tmp_board = [row[:] for row in board]
    q = deque(virus)
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if tmp_board[nx][ny] != 0:
                continue
            q.append((nx,ny))
            tmp_board[nx][ny] = 2
    safe = 0
    for row in tmp_board:
        safe += row.count(0)
    return safe


def make_wall(start,depth):
    global ans
    if depth == 3:
        ans = max(ans, bfs())
        return
    for i in range(start,len(empty)): #중복방지 start
        x,y = empty[i]
        board[x][y] = 1
        make_wall(i+1,depth+1)
        board[x][y] = 0

ans = 0
make_wall(0,0)
print(ans)