import sys
from collections import deque
input = sys.stdin.readline
#남동북서
dx = [1,0,-1,0]
dy = [0,1,0,-1]

N = int(input())
K = int(input())
board = [[0]*N for _ in range(N)]
for _ in range(K):
    a,b = map(int,input().split())
    #0-based index로 변환
    a-=1
    b-=1
    board[a][b] = 1 #사과는 1
L = int(input())
orders = []
for _ in range(L):
    X,C = input().split()
    X = int(X)
    orders.append([X,C])

def OOB(i,j):
    if i<0 or i>=N or j<0 or j>=N:
        return True
    else:
        return False

x,y = 0,0 #현재 머리의 위치
board[x][y] = 2
dir = 1 #현재 방향
time = 0
idx = 0 #order를 가리키는 인덱스
snake = deque()
snake.append([x,y])

while True:
    time += 1
    x += dx[dir]
    y += dy[dir]

    if OOB(x,y) or board[x][y] == 2: #범위를 벗어나거나 자기자신에 부딪히면
        print(time)
        break

    #뱀의 이동
    if board[x][y] == 0: #사과를 못먹었다면 꼬리 삭제
        a,b = snake.popleft() 
        board[a][b] = 0
    board[x][y] = 2 #뱀은 2로 표시
    snake.append([x,y])

    #X초가 끝난 후 뱀의 방향 전환
    if idx < L and orders[idx][0] == time:
        if orders[idx][1] == 'L':
            dir = (dir+1) % 4 #왼쪽 90도 회전
        else: #'D'
            dir = (dir+3) % 4 #오른쪽 90도 회전
        idx += 1