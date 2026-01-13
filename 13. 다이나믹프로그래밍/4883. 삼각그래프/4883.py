import sys
input = sys.stdin.readline

k = 1
while(True):
    N = int(input())
    if N == 0:
        break
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    DP = [[0]*3 for _ in range(N)] #DP[i][j] = i번째 행의 j번째 위치로 가는 최단경로
    DP[0][1] = graph[0][1]
    DP[0][2] = graph[0][2]
    DP[1][0] = graph[0][1] + graph[1][0]
    DP[1][1] = min(DP[1][0], DP[0][1], graph[0][1]+graph[0][2]) + graph[1][1]
    DP[1][2] = min(graph[0][1], graph[0][1]+graph[0][2], DP[1][1]) + graph[1][2]
    for i in range(2,N):
        DP[i][0] = min(DP[i-1][0], DP[i-1][1]) + graph[i][0]
        DP[i][1] = min(DP[i][0], DP[i-1][0], DP[i-1][1], DP[i-1][2]) + graph[i][1]
        DP[i][2] = min(DP[i][1], DP[i-1][1], DP[i-1][2]) + graph[i][2]

    print(f"{k}. {DP[N-1][1]}")
    k += 1