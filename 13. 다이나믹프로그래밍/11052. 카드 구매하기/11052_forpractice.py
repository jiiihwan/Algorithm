import sys
input = sys.stdin.readline

N = int(input())
P = [0] + list(map(int,input().split())) #1-based index
DP = [0] * (N+1) #DP[i] = 카드 i장을 살때 가능한 최대 금액

for i in range(1,N+1):
    for j in range(1, i+1):
        DP[i] = max(DP[i], DP[i-j] + P[j])
print(DP[N])