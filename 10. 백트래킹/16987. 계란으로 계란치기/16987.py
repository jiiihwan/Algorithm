import sys
input = sys.stdin.readline

N = int(input())
S,W = [],[] #내구도, 무게
for _ in range(N):
    s,w = map(int,input().split())
    S.append(s)
    W.append(w)

ans = 0
def break_egg(cur):
    global ans,S,W
    if cur == N:
        cnt = sum(1 for x in S if x <= 0)       
        ans = max(ans, cnt)
        return
    if S[cur] <= 0: #이미 깨져있으면 다음으로
        break_egg(cur+1)
        return

    can_hit = False
    for i in range(N):
        if i != cur and S[i] > 0: #자기 자신을 제외하고 안깨진 경우
            can_hit = True
            #계란치기
            S[cur] -= W[i]
            S[i] -= W[cur]
            break_egg(cur+1)
            #원상복구
            S[cur] += W[i]
            S[i] += W[cur]
    if not can_hit: #자기자신을 제외하고 모두 깨졌을 경우
        break_egg(cur+1)

break_egg(0)
print(ans)