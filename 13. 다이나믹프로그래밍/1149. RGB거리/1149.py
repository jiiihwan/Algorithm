import sys
input = sys.stdin.readline

R = [0] * 1001 #1-based index
G = [0] * 1001 #1-based index
B = [0] * 1001 #1-based index
DP = [[0] * 3 for _ in range(1001)]

N = int(input())
for i in range(1,N+1): #1-based index
    R[i], G[i], B[i] = map(int, input().split())

for i in range(1,N+1):
    DP[i][0] = min(DP[i-1][1], DP[i-1][2]) + R[i]
    DP[i][1] = min(DP[i-1][0], DP[i-1][2]) + G[i]
    DP[i][2] = min(DP[i-1][0], DP[i-1][1]) + B[i]

print(min(DP[N][0],DP[N][1],DP[N][2]))