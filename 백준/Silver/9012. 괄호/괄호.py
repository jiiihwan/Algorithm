import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    arr = input().rstrip()
    stack = []
    for a in arr:
        if not stack: #스택이 비어있으면
            stack.append(a)
            if a == ')':
                break
        elif stack[-1] == '(' and a == ')':
            stack.pop()
        else:
            stack.append(a)
    if stack: #스택에 뭐가 들어있으면
        print("NO")
    else:
        print("YES")