import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

def solve():
    left, right = 0, N-1
    ans = float('INF')
    
    while left < right:
        cur_sum = A[left] + A[right]
        if abs(cur_sum) < abs(ans):
            ans = cur_sum

        if cur_sum == 0:
            print(0)
            return
        elif cur_sum < 0:
            left += 1
        else:
            right -= 1

    print(ans)

solve()