import sys
from itertools import combinations

input = sys.stdin.readline

M, N = map(int, input().split())
universes = []

for _ in range(M):
    planet = list(map(int, input().split()))
    sorted_unique = sorted(set(planet))
    rank = {v:i for i,v in enumerate(sorted_unique)}
    compressed = tuple(rank[x] for x in planet)
    universes.append(compressed)

answer = 0
for a, b in combinations(universes, 2):
    if a == b:
        answer += 1

print(answer)
