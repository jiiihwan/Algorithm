N = int(input())
M = int(input())
fixed = [0]
for _ in range(M):
    fixed.append(int(input()))
fixed.append(N+1)
#DP[i]=i개 좌석을 섞을 수 있는 가짓수
DP = [1] * 41 
DP[1] = 1
DP[2] = 2
for i in range(3,41):
    DP[i] = DP[i-1] + DP[i-2]

ans = 1
for i in range(1,M+2):
    cnt = fixed[i] - fixed[i-1] - 1
    ans *= DP[cnt]

print(ans)