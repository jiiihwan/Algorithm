import sys

# 입력 처리
n, k = map(int, sys.stdin.readline().split())
items = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# DP 테이블 초기화 (최대 무게 K까지)
dp = [0] * (k + 1)

for w, v in items:
    # 뒤에서부터 계산하여 현재 물건이 중복 계산되는 것을 방지
    for j in range(k, w - 1, -1):
        if dp[j] < dp[j - w] + v:
            dp[j] = dp[j - w] + v

print(dp[k])