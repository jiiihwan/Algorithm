import sys
input = sys.stdin.readline

board = []
N,L = map(int,input().split())
for _ in range(N):
    board.append(list(map(int,input().split())))

ans = 0

def OOB(x,y):
    return x<0 or x>=N or y<0 or y>=N

def install_incline_ramp_for_horizental(x,y):
    cur_height = board[x][y]
    #현재칸부터 이전 L칸 동안 높이가 같으면 ramp 설치
    for i in range(L):
        #범위를 벗어났거나, 높이가 같지 않거나, 경사로가 이미 있으면 break
        if OOB(x,y-i) or cur_height != board[x][y-i] or ramp[x][y-i]: 
            break
    else:
        for i in range(L):
            ramp[x][y-i] = 1 #L칸에 ramp설치
    
def install_decline_ramp_for_horizental(x,y):
    cur_height = board[x][y+1]
    #다음칸부터 다음 L칸 동안 높이가 같으면 ramp 설치
    for i in range(1,L+1):
        #범위를 벗어났거나, 높이가 같지 않거나, 경사로가 이미 있으면 break
        if OOB(x,y+i) or cur_height != board[x][y+i] or ramp[x][y+i]:
            break
    else:
        for i in range(1,L+1):
            ramp[x][y+i] = 2 #L칸에 ramp설치

def install_incline_ramp_for_vertical(x,y):
    cur_height = board[x][y]
    #현재칸부터 이전 L칸 동안 높이가 같으면 ramp 설치
    for i in range(L):
        #범위를 벗어났거나, 높이가 같지 않거나, 경사로가 이미 있으면 break
        if OOB(x-i,y) or cur_height != board[x-i][y] or ramp[x-i][y]: 
            break
    else:
        for i in range(L):
            ramp[x-i][y] = 1 #L칸에 ramp설치

def install_decline_ramp_for_vertical(x,y):
    cur_height = board[x+1][y]
    #다음칸부터 다음 L칸 동안 높이가 같으면 ramp 설치
    for i in range(1,L+1):
        #범위를 벗어났거나, 높이가 같지 않거나, 경사로가 이미 있으면 break
        if OOB(x+i,y) or cur_height != board[x+i][y] or ramp[x+i][y]:
            break
    else:
        for i in range(1,L+1):
            ramp[x+i][y] = 2 #L칸에 ramp설치


#가로방향
ramp = [[0] * N for _ in range(N)] #0은 경사로 없음, 1은 incline, 2는 decline
for i in range(N):
    for j in range(N):
        if j == N-1:
            ans += 1 #끝까지 도달하면 성공
            break
        height_gap = board[i][j] - board[i][j+1]
        if height_gap == -1: #높이차이가 1이고 다음 것이 더 높은경우
            install_incline_ramp_for_horizental(i,j)
            if ramp[i][j] != 1: #현재 칸에 incline ramp가 없으면 break
                break
        elif height_gap == 1: #높이차이가 1이고 다음 것이 더 낮은경우
            install_decline_ramp_for_horizental(i,j)
            if ramp[i][j+1] != 2: #다음칸에 decline ramp가 없으면 break
                break
        elif height_gap == 0:
            continue
        else:
            break

#세로방향
ramp = [[0] * N for _ in range(N)] #ramp 초기화
for i in range(N):
    for j in range(N):
        if j == N-1:
            ans += 1 #끝까지 도달하면 성공
            break
        height_gap = board[j][i] - board[j+1][i]
        if height_gap == -1: #높이차이가 1이고 다음 것이 더 높은경우
            install_incline_ramp_for_vertical(j,i)
            if ramp[j][i] != 1:
                break
        elif height_gap == 1: #높이차이가 1이고 다음 것이 더 낮은경우
            install_decline_ramp_for_vertical(j,i)
            if ramp[j+1][i] != 2:
                break
        elif height_gap == 0:
            continue
        else:
            break

print(ans)