import sys
from collections import deque
input = sys.stdin.readline

def bfs(A, B):
    visited = [False] * 10000
    queue = deque()
    queue.append((A, ""))
    visited[A] = True

    while queue:
        num, cmd = queue.popleft()

        if num == B:
            return cmd

        # D
        d = (num * 2) % 10000
        if not visited[d]:
            visited[d] = True
            queue.append((d, cmd + "D"))

        # S
        s = 9999 if num == 0 else num - 1
        if not visited[s]:
            visited[s] = True
            queue.append((s, cmd + "S"))

        # L
        l = (num % 1000) * 10 + (num // 1000)
        if not visited[l]:
            visited[l] = True
            queue.append((l, cmd + "L"))

        # R
        r = (num % 10) * 1000 + (num // 10)
        if not visited[r]:
            visited[r] = True
            queue.append((r, cmd + "R"))

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(bfs(A, B))