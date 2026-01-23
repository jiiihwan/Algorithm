N, S = map(int, input().split())
nums = list(map(int, input().split()))

ans = 0

def dfs(idx, total):
    global ans

    if idx == N:
        if total == S:
            ans += 1
        return

    # 현재 숫자 선택
    dfs(idx + 1, total + nums[idx])
    # 현재 숫자 미선택
    dfs(idx + 1, total)

dfs(0, 0)

# 공집합 제거 (S == 0 인 경우)
if S == 0:
    ans -= 1

print(ans)
