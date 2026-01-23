N,M = map(int,input().split())
nums = sorted(list(map(int,input().split())))
arr = []

def backtracking(start, depth):
    if depth == M:
        print(*arr)
        return
    prev = 0
    for i in range(start,N):
        if nums[i] != prev:
            prev = nums[i]
            arr.append(nums[i])
            backtracking(i,depth+1)
            arr.pop()
	
backtracking(0,0)