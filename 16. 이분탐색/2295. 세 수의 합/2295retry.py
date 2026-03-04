import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(int(input()) for _ in range(N)))

sum_of_two = set()
for i in range(N):
    for j in range(i, N):
        sum_of_two.add(arr[i] + arr[j])

def find_max_k():
    for i in range(N-1, -1, -1): #작은거부터 찾는거보다 큰 거부터 찾는게 찾을 확률이 더 높다
        for j in range(i):
            if arr[i] - arr[j] in sum_of_two:
                return arr[i]

print(find_max_k())