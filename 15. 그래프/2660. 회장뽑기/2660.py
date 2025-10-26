import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n+1)] #1-based index
score = [52] * (n+1)

while True:
    a,b = map(int, input().split())
    if a == -1 and b == -1:
        break
    adj[a].append(b)
    adj[b].append(a)

def BFS(start):
    q = deque()
    dis = [-1] * (n+1)
    q.append(start)
    dis[start] = 0
    while q:
        cur = q.popleft()
        for nxt in adj[cur]:    
            if dis[nxt] >= 0:
                continue
            dis[nxt] = dis[cur] + 1
            q.append(nxt)
    score[start] = max(dis) #가장 큰 거리가 그 사람의 점수가 된다

for i in range(1,n+1):
    BFS(i)

minscore = min(score)
print(minscore, score.count(minscore))
for i in range(1,n+1):
    if score[i] == minscore:
        print(i, end=' ')