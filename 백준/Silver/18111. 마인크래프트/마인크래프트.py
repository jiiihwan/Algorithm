import sys
from collections import Counter

input = sys.stdin.readline

N, M, B = map(int, input().split())
# 2차원 배열 대신 1차원으로 받아서 바로 빈도수를 셉니다.
ground = []
for _ in range(N):
    ground.extend(map(int, input().split()))

# 각 높이별 개수를 카운트 (예: 높이 64인 칸이 10개)
height_counts = Counter(ground)

best_time = float('INF')
best_height = 0

# 0부터 256까지 탐색
for target_h in range(257):
    time = 0
    inventory = B

    # 맵 전체(N*M)가 아니라, 존재하는 높이들만 순회 (최대 257번)
    for current_h, count in height_counts.items():
        diff = current_h - target_h
        
        if diff > 0: # 현재 땅이 더 높음 -> 제거 (2초)
            time += diff * 2 * count
            inventory += diff * count
        elif diff < 0: # 현재 땅이 더 낮음 -> 설치 (1초)
            time += -diff * 1 * count
            inventory -= -diff * count
            
    # 모든 칸을 계산한 뒤 인벤토리가 음수가 아니면 유효
    if inventory >= 0:
        if time <= best_time: # h가 커지는 순서이므로 <=를 쓰면 가장 높은 h가 남음
            best_time = time
            best_height = target_h

print(best_time, best_height)