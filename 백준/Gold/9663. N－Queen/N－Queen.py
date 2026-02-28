N = int(input())

v1 = [False] * N #열 사용여부
v2 = [False] * (2*N-1) #우상향 대각선
v3 = [False] * (2*N-1) #좌상향 대각선

#행을 증가시켜 가면서 어떤 열에 놓을건지 결정
def backtracking(row):
    global ans
    if row == N:
        ans += 1
        return
    for col in range(N):
        if not v1[col] and not v2[row + col] and not v3[row - col + N-1]:
            v1[col] = True
            v2[row + col] = True
            v3[row - col + N-1] = True
            backtracking(row+1)
            v1[col] = False
            v2[row + col] = False
            v3[row - col + N-1] = False

ans = 0
backtracking(0)
print(ans)