import sys
from collections import deque
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

board = []
n,m = map(int,input().split())
for i in range(n):
    board.append(list(map(int,input().split())))

dist = [[-1] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            dist[i][j] = 0
        elif board[i][j] == 2:
            start_x,start_y = i,j

def bfs():
    q = deque()
    q.append([start_x,start_y])
    dist[start_x][start_y] = 0
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if dist[nx][ny] >= 0:
                continue
            if board[nx][ny] == 0:
                continue
            q.append([nx,ny])
            dist[nx][ny] = dist[x][y] + 1

bfs()
for i in range(n):
    print(*dist[i])