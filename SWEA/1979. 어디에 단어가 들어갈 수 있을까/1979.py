T = int(input())

def horizental(board,N,K):
    global ans
    for i in range(N):
        cnt = 0
        for j in range(N):
            cnt += 1
            if board[i][j] == 0:
                cnt -= 1
                if cnt == K:
                    ans += 1
                cnt = 0
            if j == N-1:
                if cnt == K:
                    ans += 1

def vertical(board,N,K):
    global ans
    for i in range(N):
        cnt = 0
        for j in range(N):
            cnt += 1
            if board[j][i] == 0:
                cnt -= 1
                if cnt == K:
                    ans += 1
                cnt = 0
            if j == N-1:
                if cnt == K:
                    ans += 1

for test_case in range(1, T + 1):
    N,K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    global ans
    ans = 0

    horizental(board,N,K)
    vertical(board,N,K)
    
    print(f"#{test_case} {ans}")