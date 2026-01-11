import sys
input = sys.stdin.readline

N,K = map(int,input().split())
bag = [list(map(int, input().split())) for _ in range(N)] # 0-based index
#DP[i][j] = 앞의 i개만 고려했을 때, 배낭 최대무게가 j일 때 얻을 수 있는 최대 가치
DP = [[0]*(K+1) for _ in range(N+1)] # 1-based index

for i in range(1,N+1):
    for j in range(1,K+1):
        if j >= bag[i-1][0]: #현재 최대무게 j보다 클 경우에만
            # 이전 값과 가장 가치가 높은 조합 중 큰 것을 대입
            # 가장 가치가 높은 조합 : 현재 물건 가치 + 이전 가방 기준 현재가방에 넣을 수 있는 무게에서의 최대 가치
            DP[i][j] = max(DP[i-1][j], bag[i-1][1] + DP[i-1][j-bag[i-1][0]])
        else:
            # 배낭 무게 초과인 경우는 이전 값 그대로 사용
            DP[i][j] = DP[i-1][j]

print(DP[N][K])