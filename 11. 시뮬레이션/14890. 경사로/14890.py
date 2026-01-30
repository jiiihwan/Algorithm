import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def check(line):
    ramp = [False] * N  # 경사로 설치 여부

    for i in range(N - 1):
        diff = line[i] - line[i + 1]

        # 높이 같음
        if diff == 0:
            continue

        # 올라가는 경사로 (다음이 1 높음)
        elif diff == -1:
            for j in range(L):
                if i - j < 0:
                    return False
                if line[i - j] != line[i]:
                    return False
                if ramp[i - j]:
                    return False
                ramp[i - j] = True

        # 내려가는 경사로 (다음이 1 낮음)
        elif diff == 1:
            for j in range(1, L + 1):
                if i + j >= N:
                    return False
                if line[i + j] != line[i + 1]:
                    return False
                if ramp[i + j]:
                    return False
                ramp[i + j] = True

        # 높이 차이 2 이상 → 실패
        else:
            return False

    return True


ans = 0

# 가로 검사
for i in range(N):
    if check(board[i]):
        ans += 1

# 세로 검사
for j in range(N):
    col = [board[i][j] for i in range(N)]
    if check(col):
        ans += 1

print(ans)