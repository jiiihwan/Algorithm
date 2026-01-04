T = int(input())

for test_case in range(1, T + 1):
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    if N > M: #A가 항상 짧은거다
        A,B = B,A
        N,M = M,N
    ans = 0
    for i in range(M-N+1):
        tmp = 0
        for j in range(N):
            tmp += A[j] * B[i+j]
        ans = max(ans, tmp)

    print(f"#{test_case} {ans}")