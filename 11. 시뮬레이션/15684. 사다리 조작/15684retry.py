import sys
input = sys.stdin.readline

N,M,H = map(int,input().split())
idx = [(i,j) for i in range(H) for j in range(N)]
board = [[-1]*N for _ in range(H)]
for _ in range(M):
    a,b = map(int,input().split())
    #0-based index로 만들기
    a -= 1
    b -= 1
    board[a][b] = b+1   
    board[a][b+1] = b

def play():
    for col in range(N):
        j = col
        i = 0
        while i < H: 
            if board[i][j] != -1:
                j = board[i][j]
            i += 1
        if j != col:
            return False
    return True

def backtracking(depth, start):
    global ans
    if depth > 3 or depth >= ans:
        return
    if play():
        ans = depth
        return

    for pos in range(start,N*H):
        i = idx[pos][0]
        j = idx[pos][1]
        if j == N-1:
            continue
        if board[i][j] == -1 and board[i][j+1] == -1: #양옆이 비어있을 때
                board[i][j] = j+1
                board[i][j+1] = j
                backtracking(depth+1, i*N+j)
                board[i][j] = -1
                board[i][j+1] = -1

ans = 4
backtracking(0,0)

if ans > 3:
    ans = -1
print(ans)