import sys
input = sys.stdin.readline

N = int(input())

T = [0] * (N+1)
P = [0] * (N+1)
D = [0] * (N+2) # 1-based index, N+1까지가 필요함

for i in range(1, N+1):
    T[i], P[i] = map(int, input().split())  

for i in range(N,0,-1): #N부터 1까지
    if i + T[i] > N + 1: #퇴사일 이후까지 시간이 걸리면
        D[i] = D[i+1]
    else:
        D[i] = max(D[i+1], D[i+T[i]] + P[i])

print(D[1])
    
'''
DP의 핵심은 문제를 잘게 쪼개는것.
D[i]는 i번째 날부터 퇴사일 까지의 최대 수익
'''