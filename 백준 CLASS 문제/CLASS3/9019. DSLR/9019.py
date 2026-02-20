import sys
from collections import deque
input = sys.stdin.readline

def bfs(A,B):
    vis = [False] * 10000
    q = deque()
    q.append((A, ""))
    vis[A] = True
    while q:
        num, cmd = q.popleft()
        if num == B:
            return cmd
        # D
        d = (num * 2) % 10000
        if not vis[d]:
            vis[d] = True
            q.append((d, cmd + "D"))
        # S
        s = 9999 if num == 0 else num - 1
        if not vis[s]:
            vis[s] = True
            q.append((s, cmd + "S"))
        # L
        l = (num % 1000) * 10 + (num // 1000)
        if not vis[l]:
            vis[l] = True
            q.append((l, cmd + "L"))
        # R
        r = (num % 10) * 1000 + (num // 10)
        if not vis[r]:
            vis[r] = True
            q.append((r, cmd + "R"))

T = int(input())
for _ in range(T):
    A,B = map(int,input().split())
    print(bfs(A,B))