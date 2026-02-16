import sys
input = sys.stdin.readline

N,M,B = map(int,input().split())
ground = [list(map(int,input().split())) for _ in range(N)]

best_time = float('INF')
best_height = 0

for h in range(257):
    time = 0
    inventory = B

    for i in range(N):
        for j in range(M):
            diff = h - ground[i][j]
            if diff < 0: #제거
                time += -diff * 2
                inventory += -diff
            elif diff > 0: #설치
                time += diff
                inventory -= diff
    if inventory >= 0:
        if best_time >= time:
            best_time = time    
            best_height = h 
print(best_time, best_height)