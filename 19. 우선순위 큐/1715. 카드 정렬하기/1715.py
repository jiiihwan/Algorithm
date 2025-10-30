import sys,heapq
input = sys.stdin.readline

N = int(input())
hq = []
for _ in range(N):
    heapq.heappush(hq, int(input()))

if N == 1:
    print(0)
else: #항상 가장 작은 것 두개를 더하는 것이 가장 좋다
    ans = 0
    while len(hq) > 1:
        a = heapq.heappop(hq)
        b = heapq.heappop(hq)
        cost = a+b
        ans += cost
        heapq.heappush(hq, cost)
print(ans)