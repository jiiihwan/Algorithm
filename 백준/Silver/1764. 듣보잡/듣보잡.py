import sys
input = sys.stdin.readline

nohear = set()
nosee = set()
N,M = map(int,input().split())
for _ in range(N):
    nohear.add(input().rstrip())
for _ in range(M):
    nosee.add(input().rstrip())

ans = []
if N <= M:
    for n in nohear:
        if n in nosee:
            ans.append(n)
else:
    for n in nosee:
        if n in nohear:
            ans.append(n)

ans.sort()
print(len(ans))
for a in ans:
    print(a)