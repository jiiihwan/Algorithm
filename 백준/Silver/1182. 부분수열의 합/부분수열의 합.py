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