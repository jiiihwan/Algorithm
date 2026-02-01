N = int(input())
arr = []
for _ in range(N):
    x,y = map(int,input().split())
    arr.append([x,y])

for i in range(N):
    k = 0
    for j in range(N):
        if i == j:
            continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            k += 1
    print(k+1, end=' ')