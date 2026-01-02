D = [[0 for _ in range(15)] for _ in range(15)] #0-based index
for i in range(15):
    D[0][i] = i #0층 초기화
for i in range(1,15):
    for j in range(1,15):
        people = sum(D[i-1][:j+1])
        D[i][j] = people

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(D[k][n])