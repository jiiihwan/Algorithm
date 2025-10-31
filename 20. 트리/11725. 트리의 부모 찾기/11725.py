import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

#1-based index
adj = [[] for _ in range(N+1)]
p = [[] for _ in range(N+1)] #parent

def dfs(cur):
    for nxt in adj[cur]:
        if p[cur] == nxt:
            continue
        p[nxt] = cur
        dfs(nxt)

for _ in range(N-1):
    a,b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

dfs(1)

for i in range(2,N+1): #2번노드부터 N번째 노드까지
    print(p[i])