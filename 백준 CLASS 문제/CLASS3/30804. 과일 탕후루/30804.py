import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
tanghuru = list(map(int,input().split()))

left = 0
ans = 0
dic = defaultdict(int)
for right in range(N):
    dic[tanghuru[right]] += 1
    while len(dic) > 2:
        dic[tanghuru[left]] -= 1
        if dic[tanghuru[left]] == 0:
            del dic[tanghuru[left]]
        left += 1
    ans = max(ans,right - left + 1)
print(ans)