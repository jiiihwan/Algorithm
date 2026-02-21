import sys
from collections import deque
input = sys.stdin.readline

dx = [1,0,-1,0,1,1,-1,-1]
dy = [0,1,0,-1,1,-1,1,-1]

while True:
    w,h = map(int,input().split())
    if w==0 and h ==0:
        break
    board = [list(map(int,input().split())) for _ in range(h)]
    vis = [[False]*w for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 0 or vis[i][j] == True:
                continue
            q = deque()
            q.append((i,j))
            vis[i][j] = True
            cnt += 1
            while q:
                x,y = q.popleft()
                for d in range(8):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if nx<0 or nx>=h or ny<0 or ny>=w:
                        continue
                    if board[nx][ny] == 0 or vis[nx][ny] == True:
                        continue
                    vis[nx][ny] = True
                    q.append((nx,ny))
    print(cnt)
