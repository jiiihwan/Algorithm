import sys
input = sys.stdin.readline

N,M = map(int, input().split())
board = [] 
for _ in range(N):
    board.append(list(map(int, input().split()))) #0-based index

#DP[i][j] 는 [0][0] ~ [i][j] 사각형 안의 누적합
DP = [[0]*(N+1) for _ in range(N+1)] #1-based index

for i in range(1,N+1):
    for j in range(1,N+1):
        DP[i][j] = DP[i][j-1] + DP[i-1][j] - DP[i-1][j-1] + board[i-1][j-1]

for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    ans = DP[x2][y2] - DP[x2][y1-1] -DP[x1-1][y2] + DP[x1-1][y1-1]
    print(ans)