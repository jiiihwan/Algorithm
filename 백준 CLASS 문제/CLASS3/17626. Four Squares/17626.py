n = int(input())
DP = [5]*50001 #DP[i] 는 i를 만들기위한 제곱수들의 최소 개수
DP[1] = 1
for i in range(2,50000):
    if i <= 223:
        DP[i**2] = 1
    DP[i] = min(DP[i], DP[i-1]+DP[1]) #DP[27] = DP[25] + DP[2]
print(DP[n])