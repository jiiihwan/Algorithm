import sys
from collections import deque
input = sys.stdin.readline

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))

bridge = deque([0] * w)
time = 0
weight_sum = 0

while trucks or weight_sum > 0:
    time += 1

    # 1) 한 칸 전진: 맨 앞이 내려감
    weight_sum -= bridge.popleft()

    # 2) 새 트럭 투입 시도
    if trucks and weight_sum + trucks[0] <= L:
        t = trucks.popleft()
        bridge.append(t)
        weight_sum += t
    else:
        bridge.append(0)

print(time)