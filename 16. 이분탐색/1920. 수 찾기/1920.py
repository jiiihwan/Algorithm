import bisect

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
num = list(map(int, input().split()))

arr.sort()
for i in range(M):
    if bisect.bisect_left(arr, num[i]) - bisect.bisect_right(arr, num[i]) == 0:
        print(0)
    else:
        print(1)