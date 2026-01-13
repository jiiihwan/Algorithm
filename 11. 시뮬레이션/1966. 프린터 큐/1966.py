import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    q = deque(map(int, input().split())) #중요도

    cnt = 0
    check = M
    while(q):
        a = q[0] #첫번째
        for i in range(len(q)):
            if a < q[i]:
                q.popleft()
                q.append(a)
                if check == 0:
                    check = len(q)-1
                else:
                    check -= 1
                break
        else: #중요도가 더 큰게 없으면
            q.popleft() #출력
            cnt += 1
            if check == 0:
                print(cnt)
                break
            else:
                check -= 1