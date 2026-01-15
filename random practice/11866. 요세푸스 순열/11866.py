from collections import deque

N,K = map(int,input().split())
q = deque()
ans = []
for i in range(1,N+1):
    q.append(i)
while q:
    for i in range(1,K+1):
        a = q.popleft()
        if i == K:
            ans.append(a)
        else:
            q.append(a)

print("<",end='')
for i in range(len(ans)-1):
    print(ans[i],end='')
    print(',',end=' ')
print(ans[-1], end='')
print(">")