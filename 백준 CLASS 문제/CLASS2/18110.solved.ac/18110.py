import sys
from collections import deque
input = sys.stdin.readline

difficulty = []
n = int(input())
for _ in range(n):
    difficulty.append(int(input()))

difficulty.sort()
difficulty = deque(difficulty) #큐로 만들기
cut = int(n * 0.15 + 0.5)#15% 절사 기준 명수, round대신 사사오입 반올림

for _ in range(cut): #절사
    difficulty.pop()
    difficulty.popleft()

if n != 0:
    ans = int(sum(difficulty)/len(difficulty) + 0.5)
else: 
    ans = 0
print(ans)