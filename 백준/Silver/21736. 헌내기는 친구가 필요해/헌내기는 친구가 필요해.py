import sys
from collections import deque
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

N,M = map(int,input().split())
board = [list(input().rstrip()) for _ in range(N)]
vis = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'I':
            doyeon_i, doyeon_j = i,j
            break
ans = 0
q = deque()
q.append([doyeon_i,doyeon_j])
vis[doyeon_i][doyeon_j] = 1
while q:
    x,y = q.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >=M:
            continue
        if vis[nx][ny] or board[nx][ny] == 'X':
            continue
        elif board[nx][ny] == 'P':
            ans += 1
        q.append([nx,ny])
        vis[nx][ny] = 1
    
if ans == 0:
    ans = 'TT'
print(ans)