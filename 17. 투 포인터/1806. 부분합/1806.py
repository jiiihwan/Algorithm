import sys
input = sys.stdin.readline

N,S = map(int, input().split())
arr = list(map(int, input().split()))

en = 0
min_length = 100001
sum = arr[0]
for st in range(N):
    while en < N and sum < S:
        en += 1
        if en != N:
            sum += arr[en]
    if en == N:
        break
    min_length = min(min_length, en-st+1)
    sum -= arr[st] #st++ 하기 전에 sum에서 st빼준다

if(min_length == 100001):
    min_length = 0

print(min_length)

