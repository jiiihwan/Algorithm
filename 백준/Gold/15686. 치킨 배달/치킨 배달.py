import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
house = []
chicken = []
picked_chicken = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            house.append((i,j))
        elif board[i][j] == 2:
            chicken.append((i,j))

#get_chicken_dist
def get_chicken_dist():
    city_chicken_dist = 0
    for r1,c1 in house:
        chick_dist = float('inf')
        for r2,c2 in picked_chicken:
            chick_dist = min(chick_dist, abs(r1-r2)+abs(c1-c2))
        city_chicken_dist += chick_dist
    return city_chicken_dist

#choose_chicken
def choose_chicken(start,cnt):
    global ans
    if cnt == M:
        ans = min(ans, get_chicken_dist())
        return
    for i in range(start, len(chicken)): #치킨집 순회
        picked_chicken.append(chicken[i])
        choose_chicken(i+1,cnt+1)
        picked_chicken.pop()

ans = float('inf')
choose_chicken(0,0)
print(ans)
