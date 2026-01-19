import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [1,-1,0,0]

N,M,x,y,K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
orders = list(map(int,input().split()))

def OOB(i,j):
    if i < 0 or i >= N or j < 0 or j >= M:
        return True
    else:
        return False
    
dice = [0,0,0,0,0,0] #동/서/북/남/위/바닥
d = [1,0,3,2]

for dir in orders:
    dir -= 1
    nx = x + dx[dir]
    ny = y + dy[dir]

    #print(f"좌표 : {nx},{ny}")

    if OOB(nx,ny):
        continue

    #dice 회전
    dice[dir],dice[5] = dice[5],dice[dir]
    dice[dir],dice[d[dir]] = dice[d[dir]],dice[dir]
    dice[dir],dice[4] = dice[4],dice[dir]
    

    if board[nx][ny] != 0: #지도에 숫자가 적혀있으면
        dice[5] = board[nx][ny] #지도에 있는거 흡수
        board[nx][ny] = 0
    else: #지도에 0이면
        board[nx][ny] = dice[5] #dice에 있는거 지도에 복사

    x = nx
    y = ny

    print(dice[4])