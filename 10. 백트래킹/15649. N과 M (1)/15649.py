N, M = map(int, input().split())

arr = [0]*M
is_used = [False]*(N+1) #1-based index

def dfs(k):
    if k == M:
        print(*arr)
        return
    for i in range(1,N+1):
        if not is_used[i]:
            arr[k] = i
            is_used[i] = True
            dfs(k+1)
            is_used[i] = False

dfs(0)