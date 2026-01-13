import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    S = [list(map(int, input().split()))] #Sticker
    S.append(list(map(int, input().split())))

    #DP[i][j] = i번째 인덱스 열의 j번째 인덱스로 끝날 때, 점수의 최댓값
    DP = [[0,0] for _ in range(n+1)] #0-based index, DP[1] 을 위해 한칸 더만들어줌
    DP[0][0] = S[0][0]
    DP[0][1] = S[1][0]
    if n != 1:
        DP[1][0] = S[1][0] + S[0][1] #1번째 열, 0번째 행으로 끝나는 경우
        DP[1][1] = S[0][0] + S[1][1] #1번째 열, 1번째 행으로 끝나는 경우
    for i in range(2,n):
        DP[i][0] = max(DP[i-1][1] + S[0][i], DP[i-2][1] + S[0][i])
        DP[i][1] = max(DP[i-1][0] + S[1][i], DP[i-2][0] + S[1][i])
        
    print(max(DP[n-1]))