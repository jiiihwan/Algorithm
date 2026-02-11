import sys
from collections import deque
input = sys.stdin.readline

dx = [1,0,-1,0,2,1,-1,-2,-2,-1,1,2]
dy = [0,1,0,-1,1,2,2,1,-1,-2,-2,-1]

K = int(input())
W,H = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(H)]

def bfs():
    global K
    q = deque()
    q.append((K,0,0)) #K,x,y
    move = [[[-1]*W for _ in range(H)] for _ in range(K+1)]
    move[K][0][0] = 0
    while q:
        k,x,y = q.popleft()
        for d in range(12):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if board[nx][ny] == 1:
                continue
            if d < 4: #상하좌우 이동
                if move[k][nx][ny] >= 0:
                    continue
                q.append((k,nx,ny))
                move[k][nx][ny] = move[k][x][y] + 1
            elif k > 0: #나이트 이동
                if move[k+1][nx][ny] >= 0: #이전 방문했던 곳은 다시 안감
                    continue
                q.append((k-1,nx,ny))
                move[k-1][nx][ny] = move[k][x][y] + 1 #k를 1소모하고 이동

            if nx == H-1 and ny == W-1:
                for i in range(H):
                    print(move[k-1][i])
                print(k)
                for i in range(H):
                    print(move[k][i])
                if d <4:
                    return move[k][H-1][W-1]
                else:
                    return move[k-1][H-1][W-1]
        print(q)

print(bfs())

