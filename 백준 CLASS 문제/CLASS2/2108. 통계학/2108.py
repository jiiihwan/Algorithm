import sys
from collections import Counter
input = sys.stdin.readline

nums = []
N = int(input())
for _ in range(N):
    nums.append(int(input()))

nums.sort()
counter = Counter(nums)

print(round(sum(nums)/N)) #반올림

print(nums[N//2]) #내림

mx = max(counter.values())
modes = sorted(k for k, v in counter.items() if v == mx)
print(modes[1] if len(modes) > 1 else modes[0])

print(max(nums)-min(nums))