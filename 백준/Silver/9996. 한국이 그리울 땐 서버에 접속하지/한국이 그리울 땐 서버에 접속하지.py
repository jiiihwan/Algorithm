import sys
input = sys.stdin.readline

N = int(input())
pattern = input()
for _ in range(N):
    is_right = True
    a = input()
    if len(pattern) - 1 > len(a):
        is_right = False
    for i in range(len(pattern)):
        if pattern[i] == '*':
            break
        else:
            if pattern[i] != a[i]:
                is_right = False
                break
    index = 0
    for i in range(len(pattern)-1,-1,-1): #*나올때까지 거꾸로 탐색
        index += 1
        if pattern[i] == '*':
            break
        else:
            if pattern[i] != a[len(a)-index]:
                is_right = False
                break

    if is_right:
        print('DA')
    else:
        print('NE')