import sys
input = sys.stdin.readline

arr = []
N = int(input())
for _ in range(N):
    num = int(input())
    arr.append(num)

arr.sort() # 오름차순 정렬
ans = 0
will_tie = False

#뒤에서 부터 두개씩 묶는다
for i in range(len(arr)-1, -1, -1):
    if arr[i] <= 0: # 0이하가 나오면 멈춤
        break
    if arr[i] == 1:
        ans += arr[i]
        continue
    if will_tie : #앞에서 묶을거라고 표시해놨으면 묶어서 곱한다
        will_tie = False
        ans -= arr[i+1]
        ans += arr[i] * arr[i+1]
    else:
        ans += arr[i]
        will_tie = True

will_tie = False
for i in range(0, len(arr), 1):
    if arr[i] > 0: # 0이상이 나오면 멈춤
        break
    if will_tie: #앞에서 묶을거라고 표시해놨으면 묶어서 곱한다
        ans -= arr[i-1]
        ans += arr[i] * arr[i-1]
        will_tie = False
    else:
        ans += arr[i]
        will_tie = True

print(ans)

'''
0. 오름차순으로 정렬
1. 뒤에서 부터 양수들은 두개씩 묶는다. 0이상 나오면 묶지않고 break
2. 앞에서 부터 음수들을 두개씩 묶는다. 0이하 나오면 묶지않고 break
'''