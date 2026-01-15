n,m = map(int, input().split())

arr1 = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(n)]
arr3 = [[1 if arr1[i][j] != arr2[i][j] else 0 for j in range(m)]for i in range(n)]

for row in arr3:
    for elem in row:
        print(elem, end=' ')
    print()

