import sys
input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int, input().split())))

ans = 0
for i in range(N - 2):
    left = i + 1
    right = N - 1
    
    while left < right:
        total = A[i] + A[left] + A[right]
        
        if total == 0:
            # 같은 값이 아닐 때
            if A[left] != A[right]:
                l_val = A[left]
                r_val = A[right]
                l_cnt = 0
                r_cnt = 0
                
                while left < right and A[left] == l_val:
                    left += 1
                    l_cnt += 1
                
                while right >= left and A[right] == r_val:
                    right -= 1
                    r_cnt += 1
                
                ans += l_cnt * r_cnt
            
            # left == right 값이 같은 경우
            else:
                count = right - left + 1
                ans += count * (count - 1) // 2
                break
        
        elif total < 0:
            left += 1
        else:
            right -= 1

print(ans)
