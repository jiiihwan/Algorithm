import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(int(input()) for _ in range(N)))

# 1. 두 수의 합(a + b) 집합 생성
sum_of_two = set()
for i in range(N):
    for j in range(i, N):
        sum_of_two.add(arr[i] + arr[j])

# 2. d - c가 집합에 있는지 확인 (큰 값부터 탐색)
def find_max_k():
    for i in range(N-1, -1, -1):
        for j in range(i):
            if arr[i] - arr[j] in sum_of_two:
                return arr[i]
    return -1

print(find_max_k())