import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

#DP[i] = i번째 까지 봤을 때 가장 긴 증가하는 부분 수열의 길이
DP = [1] * N
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            DP[i] = max(DP[i], DP[j]+1)

print(max(DP))

idx = 0
ans = []
for i in range(N-1,-1,-1):
    if DP[i] == max(DP) and idx == 0:
        ans.append(A[i])
        idx = i
    else:
        if DP[i] == DP[idx] -1:
            ans.append(A[i])
            idx = i

print(*ans[::-1])