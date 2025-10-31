import sys
input = sys.stdin.readline

def dfs(cur, parent):
    vis[cur] = 1
    for nxt in adj[cur]:
        if nxt == parent:
            continue
        if vis[nxt]:
            return True #사이클 발견
        if dfs(nxt, cur): 
            return True #상위 dfs로 발견 True 값 전파
    return False
    

case_num = 1
while True:
    n,m = map(int, input().split())
    if n == 0 and m == 0:
        break
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    
    T = 0
    vis = [0] * (n+1)
    for i in range(1, n+1): 
        if not dfs(i, 0): #만약 사이클이 없다면
            T += 1

    if T == 0:
        message = "No trees."
    elif T == 1:
        message = "There is one tree."
    else: 
        message = f"A forest of {T} trees."
    print(f"Case {case_num}: {message}")
    case_num += 1