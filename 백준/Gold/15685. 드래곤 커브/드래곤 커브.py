import sys
input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

board = [[0]*101 for _ in range(101)]

N = int(input())
for _ in range(N):
    y, x, d, g = map(int, input().split())

    dirs = [d]
    for _ in range(g):
        for i in range(len(dirs)-1, -1, -1):
            dirs.append((dirs[i] + 1) % 4)

    board[x][y] = 1
    cx, cy = x, y
    for d in dirs:
        cx += dx[d]
        cy += dy[d]
        board[cx][cy] = 1

# 정사각형 개수 세기
ans = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            ans += 1

print(ans)
