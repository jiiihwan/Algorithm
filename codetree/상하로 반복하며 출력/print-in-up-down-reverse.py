n = int(input())

arr = [[]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if j % 2 == 0: #j가 짝수일때
            print(i+1, end='')
        else:
            print(n-i, end='')
    print()