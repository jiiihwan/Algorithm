import sys
input = sys.stdin.readline

A, B = map(int, input().split())
count = 1  # 연산 횟수에 1을 더한 값을 출력해야 함

while B > A:
    if B % 2 == 0:
        B //= 2
    elif B % 10 == 1:
        B //= 10
    else:
        break
    count += 1

if B == A:
    print(count)
else:
    print(-1)