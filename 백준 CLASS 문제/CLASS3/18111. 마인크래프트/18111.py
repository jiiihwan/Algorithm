import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

best_time = int(1e18)
best_height = 0

for h in range(257):          # 목표 높이
    time = 0
    inventory = B

    for i in range(N):
        for j in range(M):
            diff = board[i][j] - h

            if diff > 0:      # 블록 제거
                time += 2 * diff
                inventory += diff
            else:             # 블록 설치
                time += -diff
                inventory += diff   # diff는 음수

    if inventory >= 0:
        if time < best_time or (time == best_time and h > best_height):
            best_time = time
            best_height = h
