from collections import deque

T = int(input())

dx = [1,0,-1,0,1,-1,-1,1]
dy = [0,1,0,-1,1,1,-1,-1]

for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    board = [[0] * N for _ in range(N)] #board 입력
    #board 초기화
    board[N//2][N//2], board[N//2-1][N//2-1] = 2, 2 #W
    board[N//2][N//2-1], board[N//2-1][N//2] = 1, 1 #B

    for _ in range(M):
        i,j,stone = map(int, input().split())

        board[i-1][j-1] = stone
        for dir in range(8):
            tmp = []
            q = deque()
            q.append([i-1,j-1])
            while q:
                curX, curY = q.popleft()
                nx = curX + dx[dir]
                ny = curY + dy[dir]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    break
                if board[nx][ny] == 0:
                    break
                elif board[nx][ny] != stone: #다른거 만나면 저장
                    tmp.append([nx,ny])
                elif board[nx][ny] == stone: #같은거 만나면 바꾸고 탈출
                    for ti,tj in tmp:
                        board[ti][tj] = stone
                    break
                q.append([nx,ny])

    black, white = 0,0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1
    print(f"#{test_case} {black} {white}")