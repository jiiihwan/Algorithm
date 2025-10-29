import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

cur = set()
en = 0
ans = 0

for st in range(n):
    while en < n and arr[en] not in cur:
        cur.add[en]
        en += 1
    res = en -st
    cur.remove(arr[st])

print(ans)