import sys
import bisect
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))
M = int(input())
num = list(map(int, input().split()))

for i in range(M):
    print(bisect.bisect_right(arr, num[i]) - bisect.bisect_left(arr, num[i]), end=' ')