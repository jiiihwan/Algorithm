T = int(input())

for test_case in range(1, T + 1):
    num = list(map(int, input().split()))

    maxnum = 0
    minnum = 10001
    cnt = 0

    for n in num:
        maxnum = max(maxnum, n)
        minnum = min(minnum, n)
        cnt += n

    cnt -= maxnum
    cnt -= minnum
    ans = cnt // 8
    if cnt / 8 - ans >= 0.5:
        ans += 1

    print(f"#{test_case} {ans}")