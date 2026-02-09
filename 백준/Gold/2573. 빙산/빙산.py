import sys
from collections import deque
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

def solve():
    def bfs(i,j):
        q = deque()
        q.append((i,j))
        vis[i][j] = 1
        while q:
            x,y = q.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0<=nx<N and 0<=ny<M:
                    if board[nx][ny] == 0 or vis[nx][ny]:
                        continue            
                    q.append((nx,ny))
                    vis[nx][ny] = 1

    year = 0
    while True:
        vis = [[0]*M for _ in range(N)]
        chunk = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] != 0 and vis[i][j] == 0: #바다가 아니고 방문 안했을 경우
                    bfs(i,j)
                    chunk += 1
        if chunk == 0: #다 녹은 경우
            print(0)
            break
        elif chunk >= 2:
            print(year)
            break

        melt = [[0]*M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if board[i][j] != 0:
                    cnt = 0
                    for d in range(4):
                        nx = i + dx[d]
                        ny = j + dy[d]
                        if nx<0 or nx>=N or ny<0 or ny>=M:
                            continue
                        if board[nx][ny] == 0:
                            cnt += 1
                    melt[i][j] = cnt
        for i in range(N):
            for j in range(M):
                if board[i][j] > 0:
                    board[i][j] = max(0, board[i][j] - melt[i][j]) 
        
        year += 1

solve()