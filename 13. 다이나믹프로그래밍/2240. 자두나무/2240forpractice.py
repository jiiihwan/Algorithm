import sys
input = sys.stdin.readline

T,W = map(int, input().split())
tree = [1] #1-based index, 1번나무가 처음 위치
for _ in range(T):
    tree.append(int(input()))
#DP[i][j] = i초까지 자두를 보았을 때, 이동을 j번 했을 때 최대 자두 개수
DP = [[0] * (W+1) for _ in range(T+1)] #1-based index

for i in range(1,T+1):
    #DP[x][0]를 위한 초기화 (한번도 움직이지 않는 경우)
    if tree[i] == 1:
        DP[i][0] = DP[i-1][0] + 1
    else:
        DP[i][0] = DP[i-1][0]

    for j in range(W+1):
        cur_tree = 1 if j % 2 == 0 else 2 #이동횟수에 따라서 현재위치 결정 
        if cur_tree == tree[i]: #현재 위치와 떨어지는 위치가 같을때
            DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]) + 1 
        else: 
            DP[i][j] = max(DP[i-1][j-1], DP[i-1][j])
print(max(DP[T]))