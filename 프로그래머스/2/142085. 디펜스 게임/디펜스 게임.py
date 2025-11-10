import heapq

def solution(n, k, enemy):
    heap = []

    for i, e in enumerate(enemy):
        heapq.heappush(heap, e)
        if len(heap) > k:
            n -= heapq.heappop(heap) # 가장 작은 건 무적권에서 빼고 병력으로 지불
        if n < 0: # 병력이 부족해지는 최초 시점
            return i

    return len(enemy)