T = int(input())

for test_case in range(1, T + 1):
    P,Q,R,S,W = map(int, input().split())
    A = P*W
    if W <= R:
        B = Q
    else:
        B = Q + S*(W-R)
    ans = min(A,B)
    print(f"#{test_case} {ans}")