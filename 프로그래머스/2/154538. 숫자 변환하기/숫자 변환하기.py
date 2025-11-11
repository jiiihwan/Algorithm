from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    
    dist = [-1] * (y+1) #1-based index
    
    q = deque()
    q.append(x)
    dist[x] = 0
    
    while q:
        cur = q.popleft()
        for nxt in (cur+n, cur*2, cur*3):
            if nxt <= y and dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                if nxt == y:
                    return dist[y]
                q.append(nxt)
    
    return -1