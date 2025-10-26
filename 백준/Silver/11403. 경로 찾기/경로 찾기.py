import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
adj = [list(map(int, input().split())) for _ in range(n)] #0-based index
vis = [False] * n
ans = [[0]*n for _ in range(n)]

#BFS
q = deque()
for i in range(n):
    q.append(i)
    vis = [False] * n
    #vis[i] = True
    #자기자신에게 돌아오는것을 체크해야하니 처음건 방문체크하지 않는다.
    while q:
        cur = q.popleft()
        for nxt in range(n): #인접리스트가 아닌 인접행렬!!
            if adj[cur][nxt] == 1 and not vis[nxt]: #
                ans[i][nxt] = 1 #nxt로 간선을 타고 갈때 표시
                q.append(nxt)
                vis[nxt] = True


for row in ans:
    print(*row)