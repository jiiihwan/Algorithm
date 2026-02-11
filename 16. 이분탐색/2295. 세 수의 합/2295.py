import sys
input = sys.stdin.readline

def solve():
    arr = []
    N = int(input())
    for _ in range(N):
        arr.append(int(input()))
    arr.sort()
    for k in range(N-1,-1,-1):
        for x in range(N):
            y,z = x,k
            while x <= y <= z <= k:
                cnt = arr[x]+arr[y]+arr[z]
                if cnt == arr[k]:
                    print(arr[k])
                    return
                elif cnt > arr[k]:
                    z -= 1
                else:
                    y += 1

solve()