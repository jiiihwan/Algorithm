N,M = map(int,input().split())
A = sorted(list(map(int,input().split())))
arr = []

def backtracking(start,depth):
    if len(arr) == M:
        print(*arr)
        return  
    prev = 0
    for i in range(start,N):
        if A[i] != prev: #같은 depth에서 A[i]를 저장하고 이로 시작하는 다른 분기는 막는다(중복방지)
            arr.append(A[i])
            prev = A[i] 
            backtracking(i+1,depth+1)
            arr.pop()

backtracking(0,0)