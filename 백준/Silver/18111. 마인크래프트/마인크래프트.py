import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]

# 2. 2차원 배열을 순회하며 빈도수(count) 계산하기
height_counts = [0] * 257
for i in range(N):
    for j in range(M):
        height_counts[ground[i][j]] += 1

best_time = float('inf')
best_height = 0

# 3. 계산 로직 (이전과 동일하게 257 * 257회 연산)
for target_h in range(257):
    time = 0
    inventory = B
    
    for current_h in range(257):
        count = height_counts[current_h]
        if count == 0: continue
        
        diff = current_h - target_h
        if diff > 0:
            time += diff * 2 * count
            inventory += diff * count
        elif diff < 0:
            time += -diff * count
            inventory -= -diff * count
            
    if inventory >= 0:
        if time <= best_time:
            best_time = time
            best_height = target_h

print(best_time, best_height)