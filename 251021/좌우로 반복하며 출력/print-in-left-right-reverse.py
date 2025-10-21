N = int(input())
arr = [[i for i in range(1,N+1)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i % 2 == 1:
            arr[i].reverse()
        print(arr[i][j],end='')
    print()