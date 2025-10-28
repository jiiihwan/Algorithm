import sys
input = sys.stdin.readline

A = []
N,M = map(int, input().split())
for _ in range(N):
    A.append(int(input()))

A.sort()


mn = 2000000001
en = 0

for st in range(N):
    while en < N and A[en] - A[st] < M:
        en += 1
    if en == N:
        break
    mn = min(mn, A[en] - A[st])

print(mn)