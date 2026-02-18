import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input().rstrip()
    n = int(input())
    nums = list(input().rstrip().split(','))
    #괄호 제거
    nums[0] = nums[0][1:]
    nums[n-1] = nums[n-1][:-1]
    #정수로 변환
    if n != 0:
        nums = list(map(int, nums))
    else:
        nums = []

    q = deque(nums)
    reverse = False
    for order in p:
        if order == 'R':
            reverse = True if reverse == False else False
        else: #D
            try:
                if reverse:
                    q.pop()
                else:
                    q.popleft()
            except:
                print('error')
                break
    else:
        nums = list(q)
        if reverse:
            nums = nums[::-1]
        print('[',end='')
        print(*nums, sep=',', end='')
        print(']')