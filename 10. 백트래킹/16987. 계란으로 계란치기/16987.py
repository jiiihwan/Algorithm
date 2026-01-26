import sys
input = sys.stdin.readline

N = int(input())
S,W = [],[] #내구도, 무게
broken = [False] * N
for _ in range(N):
    s,w = map(int,input().split())
    S.append(s)
    W.append(w)

def check_only(cur):
    global broken
    cnt = 0
    for i in range(N):
        if i != cur and broken[i]:
            cnt += 1
    if cnt == N-1:
        return True
    else:
        return False

ans = 0
def break_egg(cur,depth):
    print(depth,broken)
    global ans,S,W
    if depth == N:
        tmp = 0
        tmp += sum(broken)
        ans = max(ans, tmp)
        return

    for i in range(N):
        if i != cur and not broken[i] and not check_only(i):
            S[cur] -= W[i]
            S[i] -= W[cur]
            if S[cur] <= 0:
                broken[cur] = True
            if S[i] <= 0:
                broken[i] = True
            break_egg(cur+1, depth+1)
            S[cur] += W[i]
            S[i] += W[cur]
            if S[cur] > 0:
                broken[cur] = False
            if S[i] > 0:
                broken[i] = False
        print(broken)

break_egg(0,1)
print(ans)