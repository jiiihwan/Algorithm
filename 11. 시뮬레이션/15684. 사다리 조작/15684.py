import sys
input = sys.stdin.readline

def play():
    #사다리게임을 수행하고 result를 반환하는 함수
    result = [0]*N
    for col in range(N): #사다리
        j = col #열
        i = 0 #행
        while(i < H):
            if board[i][j] == -1:
                i += 1
            else: #사다리가 연결되어있으면 열 이동후 내려감
                j = board[i][j]
                i += 1
        result[j] = col
    return result

def backtracking(depth):
    global ans
    if play() == correct:
        ans = min(ans, depth)
        return
    if depth == len(avilable):
        return
    for i,j in avilable:
        if board[i][j] == -1 and board[i][j+1] == -1:
            board[i][j] = j+1
            board[i][j+1] = j
            backtracking(depth+1)
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
    
#가능한 가로선들
avilable = []
for i in range(H):
    for j in range(N-1):
        if board[i][j] == -1 and board[i][j+1] == -1:
            avilable.append([i,j])

ans = 300
correct = [i for i in range(N)]

backtracking(0)
print(avilable)

if ans > 3:
    ans = -1
print(ans)