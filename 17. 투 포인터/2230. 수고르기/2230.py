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
    if en == N: #while문에서 en이 n-1 일때도 en+=1 하기 때문에 종료조건이 필요하다
        break
    mn = min(mn, A[en] - A[st])

print(mn)