import sys
input = sys.stdin.readline

N = int(input())
liquid = list(map(int,input().split()))

st,en = 0,N-1
tmp_cnt = 2000000000
while st < en:
    cnt = liquid[st] + liquid[en]
    if cnt == 0:
        ansx, ansy = liquid[st], liquid[en]
        break
    elif abs(cnt) <= tmp_cnt:
        tmp_cnt = abs(cnt)
        ansx,ansy = liquid[st], liquid[en]
    if cnt > 0:
        en -= 1
    else:
        st += 1
print(ansx,ansy)