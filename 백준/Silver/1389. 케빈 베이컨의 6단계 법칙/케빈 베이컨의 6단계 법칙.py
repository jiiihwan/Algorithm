import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    if b not in adj[a]:
        adj[a].append(b)
    if a not in adj[b]:
        adj[b].append(a)

def bfs(start):
    q = deque()
    q.append(start)
    dist = [1e18]*(N+1)
    dist[start] = 0
    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if dist[nxt] < 1e18:
                continue
            q.append(nxt)
            dist[nxt] = min(dist[nxt], dist[cur]+1)
    #케빈 베이컨 수 구하기
    ans = 0
    for i in range(1,N+1):
        ans += dist[i] 
    return ans

kevin_bacon = [] 
for i in range(1,N+1):
    kevin_bacon.append(bfs(i))
print(kevin_bacon.index(min(kevin_bacon))+1)
