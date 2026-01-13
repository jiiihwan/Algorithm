import sys
input = sys.stdin.readline

DP = [0] * 1000001 #1-based index
DP[1] = 1
DP[2] = 2 # 1+1, 2
DP[3] = 4 # 1+1+1, 1+2, 2+1, 3

for i in range(4,1000001):
    DP[i] = (DP[i-1] + DP[i-2] + DP[i-3]) % 1000000009

T = int(input())
for _ in range(T):
    n = int(input())
    print(DP[n])