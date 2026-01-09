import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
reversedA = A[::-1]

inc_DP = [1] * N #DP[i] 는 i로 끝나는 가장 긴 증가하는 부분 수열의 길이
dec_DP = [1] * N #DP[i] 는 i로 끝나는 가장 긴 감소하는 부분 수열의 길이
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            inc_DP[i] = max(inc_DP[i], inc_DP[j] + 1)
        if reversedA[j] < reversedA[i]:
            dec_DP[i] = max(dec_DP[i], dec_DP[j] + 1)

dec_DP = dec_DP[::-1]
DP = [0] * N
for i in range(N):
    DP[i] = inc_DP[i] + dec_DP[i] - 1

print(max(DP))