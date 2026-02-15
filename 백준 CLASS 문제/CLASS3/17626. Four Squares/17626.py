n = int(input())
DP = [0]*(n+1) #DP[i]는 i를 만들기위한 제곱수들의 최소 개수

for i in range(1,n+1):
    DP[i] = i #1로만 구성하는 최악의 경우
    j = 1
    while j**2 <= i:
        DP[i] = min(DP[i], DP[i-j**2]+1)
        j += 1
print(DP[n])