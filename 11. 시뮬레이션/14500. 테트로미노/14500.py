import sys
from collections import deque
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
vis = [[0] * M for _ in range(N)]

def OOB(i,j):
    return True if i<0 or i>=N or j<0 or j>=M else False

def tetromino(x,y,depth,cnt): #x,y에서 출발하는 길이가 depth이고 합이 cnt인 테트로노미노
    vis[x][y] = 1
    if depth == 4:
        global ans
        ans = max(ans,cnt)
        return
    for d in range(4):
        #다음한칸
        nx = x + dx[d]
        ny = y + dy[d]
        if OOB(nx,ny):
            continue
        if vis[nx][ny] == 1:
            continue
        cnt += board[nx][ny]
        tetromino(nx,ny,depth+1,cnt)
        #다음한칸 삭제
        cnt -= board[nx][ny]
        vis[nx][ny] = 0

ans = 0
for i in range(N):
    for j in range(M):
        tetromino(i,j,0,0)
print(ans)