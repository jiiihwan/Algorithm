import sys
input = sys.stdin.readline

n,m = map(int,input().split())
trees = list(map(int, input().split()))

st,en = 0, 1000000001 #높이가 될 수 있는 범위를 지정한다
while st <= en:
    mid = (st+en)//2
    cnt = 0 #가져가는 나무의 길이를 담을 변수
    for i in trees:
        if i > mid :
            cnt += i-mid    
    if cnt >= m:
        st = mid + 1
    else:
        en = mid - 1
    
print(en)