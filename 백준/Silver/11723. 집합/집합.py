import sys
input = sys.stdin.readline

S = set()
M = int(input())
for _ in range(M):
    operation = input().split()

    if operation[0] == 'add':
        S.add(int(operation[1]))
    elif operation[0] == 'remove':
        S.discard(int(operation[1]))
    elif operation[0] == 'check':
        if int(operation[1]) in S:
            print(1)
        else:
            print(0)
    elif operation[0] == 'toggle':
        if int(operation[1]) in S:
            S.remove(int(operation[1]))
        else:
            S.add(int(operation[1]))
    elif operation[0] == 'all':
        S = {i for i in range(1,21)}
    elif operation[0] == 'empty':
        S = set()