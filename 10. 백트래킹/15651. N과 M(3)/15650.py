N,M = map(int,input().split())

arr = [0] * M

def dfs(k):
    if k == M:
        print(*arr)
        return
    for i in range(1,N+1):
        arr[k] = i #k번째 자리 업데이트
        dfs(k+1)

dfs(0)