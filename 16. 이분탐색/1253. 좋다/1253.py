import sys
input = sys.stdin.readline

N = int(input())
nums = sorted(list(map(int,input().split())))

ans = 0
for i,n in enumerate(nums):
    left, right = 0,N-1
    if left == i:
        left += 1
    if right == i:
        right -= 1
    while left < right:
        cur_sum = nums[left] + nums[right]

        if cur_sum == n:
            ans += 1
            break
        elif cur_sum < n:
            left += 1
        else:
            right -= 1
        if left == i:
            left += 1
        if right == i:
            right -= 1
print(ans)