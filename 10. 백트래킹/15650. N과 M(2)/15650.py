N,M = map(int,input().split())

arr = [0] * M
is_used = [False] * (N+1) #1-based index

def dfs(k,n): #n은 이전 자리수
    if k == M:
        print(*arr)
        return
    for i in range(1,N+1):
        if not is_used[i] and i > n:
            arr[k] = i
            is_used[i] = True
            dfs(k+1,i)
            is_used[i] = False

dfs(0,0)  