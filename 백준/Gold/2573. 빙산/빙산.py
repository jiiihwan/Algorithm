import sys
from collections import deque

#Recursion limit 설정 (DFS 사용 시 필수)
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 상하좌우 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_iceberg_count(n, m, grid):
    visited = [[False] * m for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0 and not visited[i][j]:
                # 새로운 덩어리 발견! BFS 시작
                count += 1
                queue = deque([(i, j)])
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < n and 0 <= ny < m:
                            if grid[nx][ny] > 0 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
    return count

def melt_iceberg(n, m, grid):
    # 각 칸이 얼마나 녹을지 저장
    melt_amount = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if grid[x][y] > 0:
                sea_count = 0
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                        sea_count += 1
                melt_amount[x][y] = sea_count
    
    # 실제로 녹이기
    for x in range(n):
        for y in range(m):
            grid[x][y] = max(0, grid[x][y] - melt_amount[x][y])

# 입력 처리
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

year = 0
while True:
    count = get_iceberg_count(n, m, grid)
    
    if count >= 2: # 덩어리가 2개 이상이면 성공
        print(year)
        break
    if count == 0: # 빙산이 다 녹을 때까지 분리 안 됨
        print(0)
        break
    
    melt_iceberg(n, m, grid)
    year += 1