import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
attribute = [] #0-based index
for _ in range(N):
    attribute.append(list(map(int,input().split())))

ans = 10**5
A = []
def make_team(start,depth):
    global ans
    if depth == N//2:
        B = [a for a in range(N) if a not in A]
        A_power, B_power = 0,0
        for x,y in list(permutations(A,2)):
            A_power += attribute[x][y]
        for x,y, in list(permutations(B,2)):
            B_power += attribute[x][y]
        ans = min(ans, abs(A_power - B_power))
        return
    
    #팀 나누기
    for i in range(start,N): #0-based index (0~N-1)
        A.append(i)
        make_team(i+1,depth+1)
        A.pop()

make_team(0,0)
print(ans)