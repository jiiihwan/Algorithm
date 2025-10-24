import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    
    profit = 0
    maxPrice = 0
    for i in range(N-1, -1, -1):
        if price[i] < maxPrice:
            profit += maxPrice - price[i]
        else:
            maxPrice = price[i]


    print(profit)