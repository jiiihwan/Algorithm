T = int(input())

for test_case in range(1, T + 1):
    N,M,K = map(int, input().split())
    arrive = sorted(list(map(int, input().split())), reverse=True)
    mx = max(arrive) #가장 늦게 오는 시간
    bungabbang = [0] * (mx+1)
    ans = "Possible"

    if arrive[-1] == 0: #0초 예외처리
        ans = "Impossible"

    a = len(arrive)-1
    for i in range(1,mx+1):
        bungabbang[i] = bungabbang[i-1]
        if i % M == 0:
            bungabbang[i] += K
        while a >= 0 and i == arrive[a]:
            bungabbang[i] -= 1
            a -= 1
        if bungabbang[i] < 0:
            ans = "Impossible"

    print(f"#{test_case} {ans}")