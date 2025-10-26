import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

#1-based index
adj = [[] for _ in range(n+1)]
dis = [-1] * (n+1)

for _ in range(1, m+1):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

#BFS
q = deque()
q.append(1)
dis[1] = 0 #상근이 자기 자신의 거리는 0

while q:
    cur = q.popleft()
    for nxt in adj[cur]:
        if dis[nxt] >= 0:
            continue
        dis[nxt] = dis[cur] + 1
        q.append(nxt)

ans = 0
for i in dis:
    if i > 0 and i < 3:
        ans += 1

print(ans)