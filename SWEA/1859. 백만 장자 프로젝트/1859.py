T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    stock = list(map(int, input().split()))
    profit,maxv = 0,stock[-1]
    for s in range(-1,-len(stock)-1,-1):
        if stock[s] <= maxv:
            profit += maxv - stock[s]
        else:
            maxv = stock[s]
     
    print(f'#{test_case} {profit}')