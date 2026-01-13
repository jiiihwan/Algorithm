n = int(input())

DP = [0] * (n+1) #1-based index
DP[1], DP[2] = 1, 1
for i in range(3,n+1):
    DP[i] = DP[i-1] + DP[i-2]

print(DP[n], n-2)