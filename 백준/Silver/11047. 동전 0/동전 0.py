import sys
input = sys.stdin.readline

coin = []
N,K = map(int,input().split())
for _ in range(N):
    coin.append(int(input()))

ans = 0
for i in range(N-1,-1,-1):
    if K >= coin[i]:
        ans += K // coin[i]
        K %= coin[i]
    if K == 0:
        break
print(ans)