from collections import deque

board = [list(input()) for _ in range(5)]
idx = [[i,j] for i in range(5) for j in range(5)] #1차원 인덱스를 2차원 인덱스로 변환하기 위한 배열

dx = [1,0,-1,0]
dy = [0,1,0,-1]

picked = [] #7개 뽑은 것을 담을 배열
ans = 0

def OOB(x,y):
    return x<0 or x>=5 or y<0 or y>=5
        
def is_connected():
    q = deque()
    q.append(picked[0]) #가장 첫번째를 기준으로 한다
    vis = [picked[0]]
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if OOB(nx,ny):
                continue
            if [nx,ny] not in picked or [nx,ny] in vis: #고른거 아니거나 방문했다면 넘어가기
                continue
            vis.append([nx,ny])
            q.append([nx,ny])
    return len(vis) == 7 #길이가 7이면 True

def backtracking(start, S_cnt):
    global ans
    if len(picked) == 7:
        if S_cnt >= 4 and is_connected():
            ans += 1
        return
    if 7 - len(picked) + S_cnt < 4: #남은 칸을 모두 S로 골라도 4 못채우면 종료
        return
    
    for i in range(start,25):
        x,y = idx[i]
        picked.append([x,y])
        if board[x][y] == 'S':
            backtracking(i+1, S_cnt+1)
        else:
            backtracking(i+1, S_cnt)
        picked.pop()

backtracking(0,0)
print(ans)