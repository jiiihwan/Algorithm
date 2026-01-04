from collections import deque

#D,R,U,L
dx = [1,0,-1,0]
dy = [0,1,0,-1]
dir_list = ["v",">","^","<"]

def move(board, act):
    global pos
    global dir
    dir = ["D","R","U","L"].index(act) # 0123:남동북서
    curX, curY = pos
    nx = curX + dx[dir]
    ny = curY + dy[dir]
    board[curX][curY] = dir_list[dir] #바라보는 방향 바꾸기
    if nx < 0 or nx >= H or ny < 0 or ny >= W: #맵밖을 나가면
        return
    if board[nx][ny] == '*' or board[nx][ny] == '#' or board[nx][ny] == '-': #벽이나 물이면
        return
    board[nx][ny] = board[curX][curY] #이동
    board[curX][curY] = '.' #이동했다면 지나온자리 평지화
    pos = [nx,ny]

def shoot(board, face):
    global pos
    q = deque()
    q.append(pos)
    while q:
        curX, curY = q.popleft()
        nx = curX + dx[face]
        ny = curY + dy[face]
        if nx < 0 or nx >= H or ny < 0 or ny >= W: 
            return
        if board[nx][ny] == '*': #벽돌벽을 만나면
            board[nx][ny] = '.' #평지화
            return
        if board[nx][ny] == '#': #강철벽
            return
        q.append([nx,ny])

T = int(input())

for test_case in range(1, T + 1):
    #가로세로 입력 및 보드 초기화
    H,W = map(int, input().split())
    board = [[] for _ in range(H)]
    #보드 입력 받기
    for i in range(H):
        board[i] = list(input())
    #사용자 액션 입력 받기
    N = int(input())
    actions = input()

    #전차의 현재위치,바라보는 방향 찾아서 pos에 저장
    for i in range(H):
        for j in range(W):
            if board[i][j] in dir_list:
                pos = [i,j]
                dir = dir_list.index(board[i][j]) # 0123:남동북서
    
    for act in actions:
        if act == 'S':
            shoot(board, dir)
        else:
            move(board, act)


    print(f"#{test_case}", end = ' ')
    for i in range(H):
        print(*board[i], sep='')