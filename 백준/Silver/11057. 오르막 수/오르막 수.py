N = int(input())
DP = [[0] * 10 for _ in range(N+1)] #DP[i] 는 자리수가 i면서, 마지막 숫자가 j이하로 끝나는 오르막 수의 개수 % 10007
DP[1] = [1,2,3,4,5,6,7,8,9,10]
for i in range(2,N+1):
    for j in range(10): #0부터 9까지
        if j == 0:
            DP[i][j] = DP[i-1][j] % 10007
        else:
            DP[i][j] = (DP[i-1][j] + DP[i][j-1]) % 10007

print(DP[N][9])