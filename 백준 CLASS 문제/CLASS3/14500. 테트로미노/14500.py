import sys
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
vis = [[False] * M for _ in range(N)]

def tetromino(x,y,depth,cnt): #dfs
    global ans
    if depth == 4:
        ans = max(ans, cnt)
        return
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue
        if vis[nx][ny] == True:
            continue
        vis[nx][ny] = True
        tetromino(nx,ny,depth+1,cnt+board[nx][ny])
        vis[nx][ny] = False

def check_oh(x,y):
    global ans
    neighbor = []
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue
        neighbor.append(board[nx][ny])
    
    cnt = 0
    if len(neighbor) >= 3:
        neighbor.sort(reverse=True)
        cnt = board[x][y] + sum(neighbor[:3])
    
    ans = max(ans,cnt)


ans = 0
for i in range(N):
    for j in range(M):
        vis[i][j] = True
        tetromino(i, j, 1, board[i][j])
        vis[i][j] = False

        check_oh(i,j)

print(ans)