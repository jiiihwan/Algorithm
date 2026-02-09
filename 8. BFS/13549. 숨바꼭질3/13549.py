from collections import deque

N,K = map(int,input().split())
#BFS
def BFS():
    q = deque()
    q.append(N)
    time = [-1]*100001
    time[N] = 0
    while q:
        x = q.popleft()
        for nx in [2*x,x-1,x+1]:
            if nx < 0 or nx > 100000:
                continue
            if time[nx] >= 0:
                continue
            q.append(nx)
            if nx == 2*x:
                time[nx] = time[x]
            else:
                time[nx] = time[x] + 1
            if nx == K:
                print(time[nx])
                return
if N == K:
    print(0)
else:
    BFS()