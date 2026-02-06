import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(depth, start, next):
    if next == start:
        for i in range(1,n+1):
            if tmp_team[i]:
                team[i] = True
        return
    elif depth >= n:
        return
    tmp_team[next] = True
    dfs(depth+1, start, adj[next])
    tmp_team[next] = False
        
    

T = int(input())
for _ in range(T):
    n = int(input())
    adj = [0]
    adj += list(map(int,input().split())) #1-based index to 0-based index
    team = [False] * (n+1) #0-based index
    tmp_team = [False] * (n+1) #0-based index
    for i in range(1,n+1):
        if not tmp_team[i]: #이미 true인 경우는 continue
            tmp_team[i] = True
            dfs(1,i,adj[i])
            tmp_team[i] = False
    ans = 0
    for t in team:
        if t:
            ans+=1
    print(n-ans)