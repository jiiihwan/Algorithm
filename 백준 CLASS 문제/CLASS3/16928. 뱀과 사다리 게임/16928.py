import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

# 사다리/뱀 정보 저장
ladders_and_snakes = [0] * 101 #1-based index
for _ in range(N + M):
    start, end = map(int, input().split())
    ladders_and_snakes[start] = end

def bfs():
    q = deque()
    q.append(1)
    
    dist = [-1] * 101
    dist[1] = 0
    
    while q:
        cur = q.popleft()
        
        if cur == 100:
            return dist[cur]
        
        for dice in range(1, 7):
            next_pos = cur + dice
            
            if next_pos > 100:
                continue
            
            # 사다리 or 뱀 있으면 이동
            if ladders_and_snakes[next_pos] != 0:
                next_pos = ladders_and_snakes[next_pos]
            
            if dist[next_pos] == -1:
                dist[next_pos] = dist[cur] + 1
                q.append(next_pos)

print(bfs())
