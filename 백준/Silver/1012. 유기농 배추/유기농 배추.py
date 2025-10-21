import sys
from collections import deque
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def BFS(i,j):
    Q = deque()
    vis[i][j] = 1
    Q.append([i,j])

    while Q:
        x,y = Q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if board[nx][ny] == 0 or vis[nx][ny] == 1:
                continue
            vis[nx][ny] = 1
            Q.append([nx,ny])   



T = int(input())
for _ in range(T):
    M,N,K = map(int, input().split())

    board = [[0]*M for _ in range(N)]
    vis = [[0]*M for _ in range(N)]

    for _ in range(K):
        j,i = map(int, input().split())
        board[i][j] = 1
    
    ans = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0 or vis[i][j] == 1:
                continue
            ans += 1
            BFS(i,j)
    
    print(ans)
