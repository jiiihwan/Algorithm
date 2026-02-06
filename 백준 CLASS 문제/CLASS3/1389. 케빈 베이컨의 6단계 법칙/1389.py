import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def bfs(start):
    q = deque([start])
    dist = [-1] * (N + 1)
    dist[start] = 0

    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if dist[nxt] >= 0:
			          continue 
            dist[nxt] = dist[cur] + 1
            q.append(nxt)

    return sum(dist[1:])

kevin_bacon = [] 
for i in range(1,N+1):
    kevin_bacon.append(bfs(i))
print(kevin_bacon.index(min(kevin_bacon))+1)
