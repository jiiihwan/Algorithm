A = list(input())
B = list(input())
#DP[i][j] = A의 i번째로 끝나는 수열과 B의 j번째로 끝나는 수열의 LCS길이
DP = [[0]*(len(B)+1) for _ in range(len(A)+1)] #1-based index

for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1] == B[j-1]: #A와 B배열은 0-based index이므로 보정값 -1을 넣어준다
            DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])
print(DP[-1][-1])