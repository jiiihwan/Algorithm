T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    area = [list(map(int,input().split())) for _ in range(N)]
    ans = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            for k in range(M):
                cnt += sum(area[i+k][j:j+M])
            
            ans = max(ans,cnt)
            print(ans)
    
    print(f"#{test_case} {ans}")