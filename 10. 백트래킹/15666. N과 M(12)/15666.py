N,M = map(int,input().split())
nums = sorted(list(set(map(int,input().split()))))
arr = []

def backtracking(start, depth):
    if depth == M:
        print(*arr)
        return
    for i in range(start,len(nums)):
        arr.append(nums[i])
        backtracking(i,depth+1)
        arr.pop()

backtracking(0,0)