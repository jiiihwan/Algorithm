import sys
input = sys.stdin.readline

arr = {}
N,M = map(int,input().split())
for _ in range(N):
    site, password = input().rstrip().split()
    arr[site] = password
for _ in range(M):
    print(arr[input().rstrip()])