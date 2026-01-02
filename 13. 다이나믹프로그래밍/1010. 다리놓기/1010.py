import sys
input = sys.stdin.readline

D = [[0 for _ in range(31)] for _ in range(31)] #1-based index
for i in range(1,31):
    D[i][i] = 1
for n in range(1,31):
    for m in range(n+1,31):
        D[n][m] = D[n][m-1] + n

T = int(input())
for _ in range(T):
    N,M = map(int, input().split())
    print(D[N][M])