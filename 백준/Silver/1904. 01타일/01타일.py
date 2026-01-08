N = int(input())

DP = [0] * (N+2) #1-based index
#초기화
DP[1] = 1
DP[2] = 2
for i in range(3,N+1):
    DP[i] = (DP[i-1] + DP[i-2]) % 15746
print(DP[N])