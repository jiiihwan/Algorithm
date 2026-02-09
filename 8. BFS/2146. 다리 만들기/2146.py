import sys
from collections import deque
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(i,j,board,vis,cnt):
    q = deque()
    q.append((i,j))
    vis[i][j] = True
    board[i][j] = cnt
    land = []
    land.append((i,j))
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if board[nx][ny] == 0 or vis[nx][ny]:
                continue
            q.append((nx,ny))
            land.append((nx,ny))
            vis[nx][ny] = True
            board[nx][ny] = cnt
    return land

def find_minway(land,board,vis):
    #최소거리 찾기
    ans = 300
    for l in land:
        cur = board[l[0][0]][l[0][1]]
        q = deque(l)
        dist = [[0]*N for _ in range(N)]
        while q:
            x,y = q.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if dist[nx][ny] > 0 or board[nx][ny] == cur: #방문한 경우 아니면 같은 대륙
                    continue
                if board[nx][ny] > 0 and board[nx][ny] != cur : #바다가 아니고 다른 육지를 만나면
                    ans = min(ans, dist[x][y])
                    break
                q.append((nx,ny))
                dist[nx][ny] = dist[x][y] + 1
    return ans

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

vis = [[0]*N for _ in range(N)]
land = []
#land 찾기
cnt = 0
for i in range(N):
    for j in range(N):
        if board[i][j] > 0 and not vis[i][j]:
            cnt += 1
            land.append(bfs(i,j,board,vis,cnt))
    
print(find_minway(land,board,vis))
        