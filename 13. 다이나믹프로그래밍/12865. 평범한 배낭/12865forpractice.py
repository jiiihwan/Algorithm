import sys
input = sys.stdin.readline

# 입력 처리
n, k = map(int, input().split())

# 물건 정보를 (무게, 가치) 형태로 저장 (인덱스 1부터 사용하기 위해 앞에 [0, 0] 추가)
items = [[0, 0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# dp[n+1][k+1] 테이블 초기화 (0행과 0열은 계산의 편의를 위해 0으로 둠)
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    w, v = items[i]
    for j in range(1, k + 1):
        if j < w:
            # 현재 물건을 담을 수 없는 무게라면, 이전 물건까지의 최적값을 그대로 가져옴
            dp[i][j] = dp[i - 1][j]
        else:
            # 현재 물건을 담지 않는 경우 vs 담는 경우 중 최대값 선택
            # dp[i-1][j-w] + v 는 현재 물건의 무게만큼을 비운 상태의 최적값 + 현재 가치
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[n][k])