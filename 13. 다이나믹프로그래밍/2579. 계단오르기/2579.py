import sys
input = sys.stdin.readline

N = int(input())
stairs = [0] * (N+3)
for i in range(N):
    stairs[i] = int(input())

DP = [0] * (N+3) #D[i] 는 i번째 계단을 반드시 밟았을 때 점수의 최댓값
DP[0] = stairs[0]
DP[1] = stairs[0] + stairs[1] #반드시 밟았을 때 최댓값이니 초기화는 이렇게
DP[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])
for i in range(3,N):
    DP[i] = max(DP[i-2] + stairs[i], DP[i-3] + stairs[i-1] + stairs[i])

print(DP[N-1])