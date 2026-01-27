board = [list(input()) for _ in range(5)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def OOB(x,y):
    return x<0 or x>=5 or y<0 or y>=5
        
def dfs(x,y,depth):
    global ans,som,vis
    if depth == 7:
        if som >= 4:
            ans += 1
        return
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if OOB(nx,ny):
            continue
        if vis[nx][ny]:
            continue
        vis[nx][ny] = True
        if board[nx][ny] == 'S':
            som += 1
        dfs(nx,ny,depth+1)
        vis[nx][ny] = False
        if board[nx][ny] == 'S':
            som -= 1

ans = 0
for i in range(5):
    for j in range(5):
        som = 0
        vis = [[False]*5 for _ in range(5)]
        vis[i][j] = True
        if board[i][j] == 'S':
            som += 1
        dfs(i,j,1)
        vis[i][j] = False
        if board[i][j] == 'S':
            som -= 1

print(ans)