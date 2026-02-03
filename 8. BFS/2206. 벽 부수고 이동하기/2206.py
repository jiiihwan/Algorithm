import sys
from collections import deque
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

board = []
N,M = map(int,input().split())  
for _ in range(N):
    board.append(list(map(int,input().rstrip())))

dist = [[-1]*M for _ in range(N)]

q = deque()
q.append([0,0,False])
dist[0][0] = 1
is_ans = False
while q:
    x,y,is_break = q.popleft()
    if dist[N-1][M-1] > 0:
        print(dist[N-1][M-1])
        is_ans = True
        break
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if dist[nx][ny] > 0: #방문했었다면
            continue
        if board[nx][ny] and is_break: #벽일 때 부순적이 있다면 패스
            continue
        elif board[nx][ny] and not is_break: #벽일 때 부순적없다면 부수고 이동
            q.append([nx,ny,True])
            dist[nx][ny] = dist[x][y] + 1
        else: 
            q.append([nx,ny,is_break])
            dist[nx][ny] = dist[x][y] + 1

if not is_ans:
    print(-1)