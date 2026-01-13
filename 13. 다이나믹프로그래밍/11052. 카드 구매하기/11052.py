import sys
input = sys.stdin.readline

N = int(input())
P = [0] + list(map(int,input().split())) #1-based index 로 변경
DP = [0] * (N+1) #DP[i] 는 정확히 카드 i장을 살때 가능한 최대 금액

for i in range(1,N+1): 
    for j in range(1,i+1): 
        DP[i] = max(DP[i], DP[i-j] + P[j]) #마지막에 j개들어있는 팩을 골랐을 때와 비교해서 맥시멈값을 고른다 
print(DP[N])