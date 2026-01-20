import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]

def check_line():
    global board
    line = 0
    #가로
    for i in range(5):
        if board[i] == [0,0,0,0,0]:
            line += 1
    #세로
    for i in range(5):
        tmp = 0
        for j in range(5):
            if board[j][i] == 0:
                tmp += 1
        if tmp == 5:
            line += 1
    #대각선 \
    tmp = 0
    for i in range(5):
        if board[i][i] == 0:
            tmp += 1
    if tmp == 5:
        line += 1
    #대각선 /
    tmp = 0
    for i in range(5):
        if board[i][4-i] == 0:
            tmp += 1
    if tmp == 5:
        line += 1
    return line

def change_num(num):
    global board
    for i in range(5):
        if num in board[i]:
            board[i][board[i].index(num)] = 0
            break

END = False
for i in range(5):
    for j in range(5):
        if not END:
            change_num(call[i][j])
            if check_line() >= 3:
                print(i*5 + (j+1))
                END = True
                break