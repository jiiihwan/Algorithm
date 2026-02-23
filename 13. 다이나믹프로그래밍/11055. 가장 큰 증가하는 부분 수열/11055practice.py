import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

D = A[:] #D[i] 는 i번째로 끝나는 가장 큰 증가하는 부분수열의 합

ans = 0
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            D[i] = max(D[i], D[j] + A[i])

print(max(D))