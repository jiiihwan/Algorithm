import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    clothes = defaultdict(list)
    n = int(input())
    for _ in range(n):
        cloth, kind = input().rstrip().split()
        clothes[kind].append(cloth)
    ans = 1
    for v in clothes.values():
        ans *= len(v) + 1
    ans -= 1
    print(ans)