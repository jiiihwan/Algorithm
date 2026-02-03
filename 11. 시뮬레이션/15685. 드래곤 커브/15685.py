import sys
from collections import deque
input = sys.stdin.readline

#동북서남
dx = [0,-1,0,1]
dy = [1,0,-1,0]

board = [[0] * 101 for _ in range(101)] #공용 보드
N = int(input())
for _ in range(N):
    y,x,d,g = map(int,input().split())
    dragon_curve = [[0] * 101 for _ in range(101)] #드래곤 커브 초기화
    #0세대
    dragon_curve[x][y] = 1 
    dragon_curve[x+dx[d]][y+dy[d]] = 1 
    save_generation = [[x,y], [x+dx[d], y+dy[d]]]
    #끝점 저장
    endx = x+dx[d]
    endy = y+dy[d]
    if g > 0:
        for i in range(1,g+1):
            tmp = []
            for ix, iy in save_generation:
                #끝점을 빼서 원점으로 옮김
                ix -= endx
                iy -= endy
                #90도 돌리기
                ix,iy = iy,-ix
                #다시 끝점 더해주기
                ix += endx
                iy += endy
                dragon_curve[ix][iy] = 1 #드래곤 커브 업데이트
                if [ix,iy] not in save_generation:
                    tmp.append([ix,iy])
            save_generation += tmp #다음세대에 넘겨주기

            #세대의 끝점 업데이트
            #시작점이 끝점 기준으로 돌리고나면 새로운 끝점이 된다.
            print(save_generation, g, endx,endy)
            endx, endy = save_generation[2**g][0], save_generation[2**g][1]

    #세대가 끝나면 공용보드에 업데이트
    for i in range(101):
        for j in range(101):
            if dragon_curve[i][j] == 1:
                board[i][j] = 1

#정사각형의 네 꼭짓점이 드래곤커브의 일부인 것을 찾기
ans = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            ans += 1
print(ans)

for i in range(10):
    print(board[i][:10])