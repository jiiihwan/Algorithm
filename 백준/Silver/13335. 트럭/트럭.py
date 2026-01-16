import sys
from collections import deque
input = sys.stdin.readline

n,w,L = map(int,input().split())
trucks = list(map(int,input().split()))

ans,weight_sum = 0,0
br = deque()
for _ in range(w):
    br.append(0) #무게 0인 트럭들로 채우기

i = 0 #트럭 조회용 인덱스
while True:
    if i >= n and weight_sum == 0:
        break
    elif i < n and weight_sum+trucks[i] <= L: #이번 트럭이 올라갔을 때 무게 제한 이내라면
        weight_sum -= br.popleft()
        br.append(trucks[i])
        ans += 1
        weight_sum += trucks[i]
        i += 1
    else:
        weight_sum -= br.popleft()
        if i < n and weight_sum+trucks[i] <= L:
            br.append(trucks[i])
            weight_sum += trucks[i]
            i += 1
        else:
            br.append(0)
        ans += 1

print(ans)