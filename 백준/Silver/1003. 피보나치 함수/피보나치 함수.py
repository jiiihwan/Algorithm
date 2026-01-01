import sys
input = sys.stdin.readline


f = [[0,0] for _ in range(41)]  #0-based index
f[0] = [1,0]
f[1] = [0,1]

for i in range(2,41):
    f[i][0] = f[i-1][0] + f[i-2][0]
    f[i][1] = f[i-1][1] + f[i-2][1]

T = int(input())
for _ in range(T):
    N = int(input())
    print(f[N][0], f[N][1])
