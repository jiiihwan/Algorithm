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
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)

    return sum(dist[1:])

answer = 1
min_bacon = bfs(1)

for i in range(2, N + 1):
    bacon = bfs(i)
    if bacon < min_bacon:
        min_bacon = bacon
        answer = i

print(answer)
