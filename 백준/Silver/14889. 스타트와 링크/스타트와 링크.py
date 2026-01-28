import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
attribute = [] #0-based index
for _ in range(N):
    attribute.append(list(map(int,input().split())))

ans = 10**5
team_start = [0] #팀 중복 방지, 0번째 사람을 항상 넣어 놓는다
def make_team(start,depth):
    global ans
    if depth == N//2:
        team_link = [a for a in range(N) if a not in team_start]
        start_sum, link_sum = 0,0
        for i in range(len(team_start)):
            for j in range(i+1,len(team_start)):
                x,y = team_start[i], team_start[j]
                start_sum += attribute[x][y] + attribute[y][x]
        for i in range(len(team_link)):
            for j in range(i+1,len(team_link)):
                x,y = team_link[i], team_link[j]
                link_sum += attribute[x][y] + attribute[y][x]

        ans = min(ans, abs(start_sum - link_sum))
        return
    
    #팀 나누기
    for i in range(start,N): #0-based index (0~N-1)
        team_start.append(i)
        make_team(i+1,depth+1)
        team_start.pop()

make_team(1,1) #이미 0번째 사람 넣어놨으니 1부터 시작
print(ans)