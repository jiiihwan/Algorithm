import sys
input = sys.stdin.readline

n = int(input())
lines = [0] * (501) #1-based index, 몇번 전깃줄이 몇번에 연결되어있는지를 저장할 배열
for _ in range(n):
    a,b = map(int,input().split())
    lines[a] = b #a번 전깃줄에 연결된 줄은 b번

mx = max(lines)
DP = [1] * (mx+1) #DP[i] 는 i로 끝나는 가장 긴 부분 증가 수열의 길이
for i in range(1,mx+1):
    for j in range(1,i):
        if lines[j] < lines[i] and lines[j] != 0:
            DP[i] = max(DP[i], DP[j]+1)

print(n-max(DP))