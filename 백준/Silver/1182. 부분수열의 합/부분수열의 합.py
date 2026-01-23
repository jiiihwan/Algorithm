N, S = map(int, input().split())
nums = list(map(int, input().split()))

arr = []
ans = 0

def backtracking(start, depth, current_sum):
    global ans

    if arr and current_sum == S:
        ans += 1

    if depth == N:
        return

    for i in range(start, N):
        arr.append(nums[i])
        backtracking(i + 1, depth + 1, current_sum + nums[i])
        arr.pop()

backtracking(0, 0, 0)
print(ans)
