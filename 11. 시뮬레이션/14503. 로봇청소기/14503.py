import sys
from collections import deque
input = sys.stdin.readline

#북동남서
dx = [-1,0,1,0]
dy = [0,1,0,-1]


N,M = map(int,input().split())
r,c,dir = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
vis = [[0]*M for _ in range(N)]

q = deque()
q.append([r,c])
vis[r][c] = 1
ans = 1
while q:
    curX,curY = q.popleft()

    #주변 4칸 탐색
    is_dirty = False #주변 4칸중 청소할 칸이 있으면 True
    for d in range(4):
        nx = curX + dx[d]
        ny = curY + dy[d]
        if board[nx][ny] == 1 or vis[nx][ny] > 0: #벽이거나 방문한 경우
            continue
        else:
            is_dirty = True
            break

    if not is_dirty: #청소 안해도 되면
        dir = (dir+2) % 4 # 후진방향
        nx = curX + dx[dir]
        ny = curY + dy[dir]
        if board[nx][ny] == 0: #벽이 아니라 후진가능하면
            q.append([nx,ny])
            dir = (dir+2) % 4 #바라보는 방향 원상복구
        else:
            break
    else: #청소해야하면
        dir = (dir-1) % 4 #90도 반시계회전
        nx = curX + dx[dir]
        ny = curY + dy[dir]
        if board[nx][ny] == 0 and vis[nx][ny] == 0: #벽아니 방문 안했으면
            vis[nx][ny] = vis[curX][curY] + 1
            ans += 1
            q.append([nx,ny]) #전진
            continue
        q.append([curX,curY]) #전진하지 못한 경우 제자리에서 다시 탐색

print(ans)