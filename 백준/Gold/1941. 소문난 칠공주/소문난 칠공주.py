from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]
idx = [(i,j) for i in range(5) for j in range(5)]

board = [list(input().rstrip()) for _ in range(5)]
princess = [] #뽑은 공주들의 좌표를 담는 배열
S_cnt = 0

def is_connected():
    q = deque()
    q.append(princess[0])
    vis = [princess[0]]
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx<0 or nx>=5 or ny<0 or ny>=5:
                continue
            if (nx,ny) in vis or (nx,ny) not in princess: #방문했거나 뽑은게 아니라면
                continue
            q.append((nx,ny))
            vis.append((nx,ny))
    return len(vis) == 7

#25개 학생 중에 7개를 뽑는 함수
def backtracking(start,S_cnt):
    global ans
    if 7- len(princess) + S_cnt < 4: #아예 안되는 경우 미리 가지치기
        return
    if len(princess) == 7:
        if S_cnt >= 4 and is_connected():
            ans += 1
        return
    for i in range(start,25): #뽑는 집단
        x,y = idx[i]
        if board[x][y] == 'S':
            S_cnt += 1
        princess.append(idx[i])
        backtracking(i+1,S_cnt)
        if board[x][y] == 'S':
            S_cnt -= 1
        princess.pop()

ans = 0
backtracking(0,0)
print(ans)