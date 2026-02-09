import sys
input = sys.stdin.readline

lan = []
K,N = map(int,input().split())
for _ in range(K):
    lan.append(int(input()))

st,en = 1,max(lan)
while st <= en:
    mid = (st + en) // 2
    cnt = 0
    for l in lan:
        cnt += l // mid
    if cnt >= N:
        ans = mid
        st = mid + 1
    else:
        en = mid - 1
print(ans)