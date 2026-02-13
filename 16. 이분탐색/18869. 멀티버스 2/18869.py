import sys
from collections import defaultdict
input = sys.stdin.readline

M,N = map(int,input().split())
multiverse = defaultdict(int)
for _ in range(M):
    planet = list(map(int,input().split()))
    sorted_planet = sorted(set(planet)) #sorted에는 리스트로 바꾸는 기능이 있다!

    indices = {v:i for i,v in enumerate(sorted_planet)} #값:인덱스
    
    new_planet = tuple(indices[x] for x in planet)
    
    multiverse[new_planet] += 1 #이 튜플의 개수 세기

ans = 0
for v in multiverse.values():
    ans += v * (v-1) // 2
print(ans)