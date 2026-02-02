import sys
input = sys.stdin.readline

def play():
    for col in range(N): #사다리
        j = col #열
        i = 0 #행
        for i in range(H):
            if board[i][j] != -1:
                j = board[i][j]
        if j != col:
            return False
    return True

def backtracking(depth, start_i, start_j):
    global ans
    if depth > 3 or depth >= ans:
        return
    if play():
        ans = depth
        return

    for i in range(start_i, H):
        for j in range(N-1):
            if i == start_i and j < start_j:
                continue
            if board[i][j] == -1 and board[i][j+1] == -1: #양옆이 비어있을 때
                board[i][j] = j+1
                board[i][j+1] = j
                backtracking(depth+1, i, j)
                board[i][j] = -1
                board[i][j+1] = -1


N,M,H = map(int,input().split())
board = [[-1]*N for _ in range(H)]
for _ in range(M):
    a,b = map(int,input().split())
    #0-based index로 만들기
    a -= 1
    b -= 1
    board[a][b] = b+1   
    board[a][b+1] = b

ans = 4
backtracking(0,1,1)

if ans > 3:
    ans = -1
print(ans)