import sys
input = sys.stdin.readline

N,M = map(int, input().split())
A = list(map(int, input().split()))

en = 0
ans = 0
sum = A[0]
for st in range(N):
    while en < N and sum < M:
        en += 1
        if en != N:
            sum += A[en]
    if en == N:
        break
    if sum == M:
        ans += 1
    sum -= A[st]

print(ans)