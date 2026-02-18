import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().rstrip()
    n = int(input())
    arr = input().rstrip()[1:-1]  # 대괄호 제거
    
    if arr:
        q = deque(map(int, arr.split(',')))
    else:
        q = deque()
    
    reverse = False
    
    for cmd in p:
        if cmd == 'R':
            reverse = not reverse
        else:  # D
            if not q:
                print("error")
                break
            
            if reverse:
                q.pop()
            else:
                q.popleft()
    else:
        if reverse:
            q.reverse()
        
        print('[' + ','.join(map(str, q)) + ']')
