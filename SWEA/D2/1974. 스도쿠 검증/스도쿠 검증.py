T = int(input())

right = {1,2,3,4,5,6,7,8,9}

def horizental(board):
    temp = set()
    for i in range(9):
        for j in range(9):
            temp.add(board[i][j])
        if temp != right:
            return False
        temp.clear()
    return True

def vertical(board):
    temp = set()
    for i in range(9):
        for j in range(9):
            temp.add(board[j][i])
        if temp != right:
            return False
        temp.clear()
    return True

def cube(board,x,y):
    temp = set()
    for i in range(3):
        for j in range(3):
            temp.add(board[x+i][y+j])
    if temp != right:
        return False
    return True

for test_case in range(1, T + 1):
    ans = 1
    board = [list(map(int, input().split())) for _ in range(9)]

    if not horizental(board) or not vertical(board):
        ans = 0
    for i in [0,3,6]:
        for j in [0,3,6]:
            if not cube(board,i,j):
                ans = 0

    print(f"#{test_case} {ans}")