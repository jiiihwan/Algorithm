import sys
input = sys.stdin.readline

DP = [[[0] * 21 for _ in range(21)] for _ in range(21)] #0-based index
for i in range(21):
    for j in range(21):
        for k in range(21):
            if i == 0 or j == 0 or k == 0:
                DP[i][j][k] = 1

for i in range(1,21):
    for j in range(1,21):
        for k in range(1,21):
            if i < j and j < k:
                DP[i][j][k] = DP[i][j][k-1] + DP[i][j-1][k-1] - DP[i][j-1][k]
            else:
                DP[i][j][k] = DP[i-1][j][k] + DP[i-1][j-1][k] + DP[i-1][j][k-1] - DP[i-1][j-1][k-1]

while(True):
    a,b,c = map(int,input().split())
    if a == b == c == -1:
        break
    aa,bb,cc = a,b,c
    if a <= 0 or b <= 0 or c <= 0:
        aa,bb,cc = 0,0,0
    elif a > 20 or b > 20 or c > 20:
        aa,bb,cc = 20,20,20
    print(f"w({a}, {b}, {c}) = {DP[aa][bb][cc]}")