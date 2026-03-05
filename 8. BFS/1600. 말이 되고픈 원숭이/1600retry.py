import sys
from collections import deque
input = sys.stdin.readline

# 상하좌우 이동
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 말 이동
hdx = [-2, -2, -1, -1, 1, 1, 2, 2]
hdy = [-1, 1, -2, 2, -2, 2, -1, 1]

K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]

# vis[x][y][k] = (x, y)에 말 이동을 k번 써서 도착했을 때의 최소 동작 수
dist = [[[-1]*(K+1) for _ in range(W)] for _ in range(H)]

def solve():
    q = deque()
    q.append((0,0,0))
    dist[0][0][0] = 0
    while q:
        x, y, used_k = q.popleft()
        if x == H-1 and y == W-1:
            return dist[x][y][used_k]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx<0 or nx>=H or ny<0 or ny>=W:
                continue
            if board[nx][ny] == 1 or dist[nx][ny][used_k] >= 0:
                continue
            dist[nx][ny][used_k] = dist[x][y][used_k] + 1
            q.append((nx,ny,used_k))
        if used_k < K:
            for d in range(8):
                nx = x + hdx[d]
                ny = y + hdy[d]
                if nx<0 or nx>=H or ny<0 or ny>=W:
                    continue
                if board[nx][ny] == 1 or dist[nx][ny][used_k+1] >= 0:
                    continue
                dist[nx][ny][used_k+1] = dist[x][y][used_k] + 1
                q.append((nx,ny,used_k+1))
    return -1

print(solve())