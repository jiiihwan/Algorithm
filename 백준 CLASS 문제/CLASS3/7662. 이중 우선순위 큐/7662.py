import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    min_pq = []
    max_pq = []
    k = int(input())
    vis = [False] * k #삽입이 되었으면 True
    for i in range(k):
        cmd, num = input().split()
        num = int(num)
        if cmd == 'I':
            heapq.heappush(min_pq,(num,i))
            heapq.heappush(max_pq,(-num,i))
            vis[i] = True #i번째 수는 삽입처리
        else: #D
            if num == 1: #최댓값 삭제
                while max_pq and not vis[max_pq[0][1]]:
                    heapq.heappop(max_pq)
                if max_pq:
                    vis[max_pq[0][1]] = False
                    heapq.heappop(max_pq)
            else: #최솟값 삭제
                while min_pq and not vis[min_pq[0][1]]:
                    heapq.heappop(min_pq)
                if min_pq:
                    vis[min_pq[0][1]] = False
                    heapq.heappop(min_pq)

    while max_pq and not vis[max_pq[0][1]]:
        heapq.heappop(max_pq)
    while min_pq and not vis[min_pq[0][1]]:
        heapq.heappop(min_pq)

    if max_pq and min_pq:
        mx = -max_pq[0][0]
        mn = min_pq[0][0]
        print(mx,mn)
    else:
        print("EMPTY")