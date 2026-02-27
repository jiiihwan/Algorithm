import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    
    dp = [[0]*(N+1) for _ in range(M+1)]
    
    for i in range(M+1):
        dp[i][0] = 1
        
    for i in range(1, M+1):
        for j in range(1, min(i, N)+1):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            
    print(dp[M][N])