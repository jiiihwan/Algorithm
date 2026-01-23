N, S = map(int, input().split())
nums = list(map(int, input().split()))

ans = 0

def backtracking(idx, total):
    global ans

    if idx == N:
        if total == S:
            ans += 1
        return

    # 현재 숫자 선택
    backtracking(idx + 1, total + nums[idx])
    # 현재 숫자 미선택
    backtracking(idx + 1, total)

backtracking(0, 0)

# 공집합 제거 (S == 0 인 경우)
if S == 0:
    ans -= 1

print(ans)




'''
N,S = map(int,input().split())
nums = sorted(list(map(int,input().split())))
arr = []
ans = 0

def backtracking(start,depth):
    global ans
    #print(arr, sum(arr))
    if arr and sum(arr) == S:
        ans += 1
    if depth == N:
        return
    for i in range(start,N):
        arr.append(nums[i]) 
        backtracking(i+1,depth+1)
        arr.pop()

backtracking(0,0)
print(ans)  
'''