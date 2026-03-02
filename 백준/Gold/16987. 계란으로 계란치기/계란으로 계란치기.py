import sys
input = sys.stdin.readline

N = int(input())
S,W = [],[] #내구도, 무게
for _ in range(N):
    s,w = map(int,input().split())
    S.append(s)
    W.append(w)

def break_egg(cur):
    global ans
    if cur == N:
        cnt = 0
        for s in S:
            if s <= 0:
                cnt += 1 
        ans = max(ans, cnt)
        return
    if S[cur] <= 0: #손에 든 계란이 깨진 경우는 바로 다음으로 넘어간다
        break_egg(cur+1)
        return
    can_hit = False #때릴 수 있는 계란이 있는가?
    for i in range(N):
        if i != cur and S[i] > 0: #자기자신은 제외, 깨려고 하는 계란이 안깨진 경우에만
            can_hit = True
            S[cur] -= W[i]
            S[i] -= W[cur]
            break_egg(cur+1)
            S[cur] += W[i]
            S[i] += W[cur]
    if not can_hit: #때릴 수 있는 계란이 아무것도 없을 경우 위 for문이 실행되지 않으므로 예외처리
        break_egg(cur+1)

ans = 0
break_egg(0)
print(ans)