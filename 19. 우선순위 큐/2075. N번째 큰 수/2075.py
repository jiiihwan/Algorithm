import sys, heapq
input = sys.stdin.readline

hq = []
N = int(input())

for _ in range(N):
    for i in list(map(int, input().split())):
        if len(hq) < N:
            heapq.heappush(hq, i)
        else:
            if hq[0] < i:
                heapq.heappop(hq)
                heapq.heappush(hq, i)
print(hq[0])

'''
N번째 큰수를 구하는게 핵심
힙에는 N개의 수만 담는다. N개의 수 중에서 가장 작은 수가 N번째 큰수가 된다.
N개 채울때까지는 일단 담고
다 채웠으면 N개 중에서 최소값이랑 비교해서 더 크면 담는다.
'''