import sys
import bisect
input = sys.stdin.readline

nA,nB = map(int, input().split())
A = sorted(list(map(int,input().split()))) #오름차순으로 출력해야하니 정렬
B = sorted(list(map(int,input().split()))) #bisect를 써야하니 정렬

ans = []
for i in A:
    if bisect.bisect_right(B, i) - bisect.bisect_left(B, i) == 0: #존재하지않으면
        ans.append(i)
    else:
        continue

if ans: #안비어있으면
    print(len(ans))
    print(*ans)
else:
    print(0)
