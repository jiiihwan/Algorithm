import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
#D[i]는 i번째로 끝나는 증가하는 부분수열의 합
D = A[:] #혼자 시작하는 경우를 생각하여 초기화를 A로 얕은 복사한다.

#전체 순회
for i in range(N):
    #순회한 곳 이전까지 순회하면서
    for j in range(i):
        if A[j] < A[i]: #증가하는 부분 수열일 때만 계산, 증가하지 않는 경우는 건너뛴다
            D[i] = max(D[i], A[i] + D[j])

print(max(D))

#DP의 특성을 잘 생각하자!
#증가하는 부분수열에 증가하는게 오면 거기다가 추가로붙이면 끝