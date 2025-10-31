import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

#1-based index
adj = [[] for _ in range(N+1)]
p = [0] * (N+1) #parent

def dfs(cur):
    for nxt in adj[cur]:
        if p[cur] == nxt: #nxt가 현재노드의 부모라면 뛰어넘기
            continue
        p[nxt] = cur #다음 노드의 부모는 현재노드이다
        dfs(nxt)

for _ in range(N-1):
    a,b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

dfs(1)

for i in range(2,N+1): #2번노드부터 N번째 노드까지
    print(p[i])