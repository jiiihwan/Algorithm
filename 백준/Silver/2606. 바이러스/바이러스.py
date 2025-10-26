import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

adj = [[] for _ in range(n+1)] #1-based index 2차원 배열 초기화
vis = [False] * (n+1)

for _ in range(1,m+1):
    u,v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

#BFS
q = deque()
q.append(1)
vis[1] = True
num = -1
while q:
    cur = q.popleft()
    num += 1
    for nxt in adj[cur]:
        if vis[nxt]:
            continue
        vis[nxt] = True
        q.append(nxt)

print(num)
    