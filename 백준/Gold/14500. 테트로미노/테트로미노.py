import sys

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 보드 전체 최댓값
mx = max(map(max, board))
ans = 0

def dfs(depth, temp, lst):
    global ans
    
    # 가지치기 (이게 성능의 핵심!)
    if temp + (4 - depth) * mx <= ans:
        return
    
    if depth == 4:
        ans = max(temp, ans)
        return

    # 지금까지 선택된 모든 칸 주변을 탐색 (ㅗ 모양 포함 모든 모양 가능)
    for i in range(len(lst)):
        x, y = lst[i]
        for dx, dy in [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]:
            if 0 <= dx < n and 0 <= dy < m and board[dx][dy] > 0:
                val = board[dx][dy]
                board[dx][dy] *= -1 # 방문 표시
                # 지금까지의 리스트에 새 좌표 추가하여 전달
                dfs(depth + 1, temp + val, lst + [(dx, dy)])
                board[dx][dy] *= -1 # 원상 복구

for i in range(n):
    for j in range(m):
        start_val = board[i][j]
        board[i][j] *= -1 # 이 칸을 포함하는 모든 조합을 찾을 것이므로 영구 표시
        dfs(1, start_val, [(i, j)])
        # 여기서 원상복구를 하지 않아야 중복 탐색이 제거됩니다.

print(ans)