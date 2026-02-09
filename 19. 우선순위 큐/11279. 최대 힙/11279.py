import sys
import heapq
input = sys.stdin.readline

h = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        if h == []:
            print(0)
        else:
            print(-heapq.heappop(h))
    else:
        heapq.heappush(h, -x)