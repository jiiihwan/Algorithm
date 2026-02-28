import sys
from collections import deque
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]

def bfs():
    dist = [[[-1]*2 for _ in range(M)] for _ in range(N)] #안부수고 도달, 부수고 도달 2가지 상태 저장용 3차원 배열
    q = deque()
    q.append((0,0,0)) #x,y,벽부숨 여부(0은 안부숨, 1은 부숨)
    dist[0][0][0] = 1
    while q:
        x,y,is_break = q.popleft()
        if x == N-1 and y == M-1:
            return dist[x][y][is_break]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx<0 or nx>=N or ny<0 or ny>=M: #범위 나가면 패스
                continue
            if dist[nx][ny][is_break] == -1 and board[nx][ny] == 0:
                q.append((nx,ny,is_break))
                dist[nx][ny][is_break] = dist[x][y][is_break] + 1
            elif dist[nx][ny][1] == -1 and board[nx][ny] == 1 and is_break == 0:
                q.append((nx,ny,1))
                dist[nx][ny][1] = dist[x][y][0] + 1
    return -1

print(bfs())