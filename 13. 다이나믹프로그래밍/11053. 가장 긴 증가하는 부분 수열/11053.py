N = int(input())
A = list(map(int, input().split()))

DP = [1] * N #DP[i]는 i로 끝나는 가장 긴 증가하는 부분 수열의 길이
for i in range(N):
    for j in range(i):
        if A[i] > A[j]: #증가하는 부분수열일때
            DP[i] = max(DP[i], DP[j] + 1)
print(max(DP))