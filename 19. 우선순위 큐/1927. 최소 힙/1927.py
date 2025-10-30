import sys, heapq
input = sys.stdin.readline

hq = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        if not hq:
            print(0)
        else:
            print(heapq.heappop(hq))
    else:
        heapq.heappush(hq, x)