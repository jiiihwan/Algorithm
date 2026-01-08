import sys
input = sys.stdin.readline

n = int(input())
grape = [0] * (n+2) #0-based index
for i in range(n):
    grape[i] = int(input())

DP = [0] * (n+2) #DP[i]는 i번째 포도주를 마셨을 때 이때까지 마신 포도주의 최대량
DP[0] = grape[0]
DP[1] = grape[0] + grape[1]
for i in range(2,n):
    #경우의 수
    #1. 3번째전, 1번째전, 지금 (연속해서 마시는 경우)
    #2. 2번째전, 지금 (뛰어넘어서 마시는 경우)
    #3. 안마시기 (이전꺼 그대로쓰기 -> 다음의 큰 걸 보기위함)
    DP[i] = max(DP[i-3]+grape[i-1]+grape[i], DP[i-2]+grape[i], DP[i-1])

print(DP[n-1])