import sys
input = sys.stdin.readline

m,n = map(int,input().split())
snack = list(map(int, input().split()))

st,en = 1, max(snack)
while st <= en:
    mid = (st+en)//2 #실험할 길이
    cnt = 0 #mid길이로 잘랐을때 몇개가 나오는지 담을 변수
    for i in snack: #진짜 잘라보는 과정
        cnt += i//mid
    if cnt >= m: #더 많이 나왔다면 더 길게 잘라도 된다.
        st = mid + 1
    else:
        en = mid - 1
        
print(en)