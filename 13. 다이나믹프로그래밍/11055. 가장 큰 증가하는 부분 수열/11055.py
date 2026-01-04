import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
D = [0] * N
D[0] = A[0]
mn = A[0]

for i in range(N-1):
    if A[i] < A[i+1]:
        D[i+1] = D[i] + A[i+1]
    elif A[i] >= A[i+1]:
        if mn <= A[i+1]:
            D[i+1] = mn + A[i+1]
        else:
            D[i+1] = A[i+1]
        mn = min(mn,A[i])

print(max(D))
print(D)