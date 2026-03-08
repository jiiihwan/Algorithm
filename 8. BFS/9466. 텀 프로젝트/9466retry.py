import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(x):
    global cnt
    visited[x] = True
    nxt = adj[x]

    if not visited[nxt]:
        dfs(nxt)
    elif not finished[nxt]:
        # 사이클 발견
        cur = nxt
        cnt += 1
        while cur != x:
            cur = adj[cur]
            cnt += 1
    finished[x] = True

T = int(input())
for _ in range(T):
    n = int(input())
    adj = [0] + list(map(int, input().split())) #1-based index
    #1-based index
    visited = [False] * (n + 1)
    finished = [False] * (n + 1)
    cnt = 0  # 사이클에 속한 학생 수

    for i in range(1, n + 1): #1~n학생까지
        if not visited[i]:
            dfs(i)

    print(n - cnt)
