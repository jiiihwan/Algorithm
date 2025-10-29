n = int(input())

#에라토스테네스의 체
primes = [True] * (n+1)
primes[0] = primes[1] = False

for i in range(2, int(n**0.5) + 1):
    if primes[i]:
        for j in range(i*i, n+1, i): #i의 제곱부터 끝까지, 배수만큼 뛰어넘으며
            primes[j] = False

primes = [i for i in range(2,n+1) if primes[i]]

#투 포인터로 부분합 구하면서 탐색
en,ans, = 0,0
length = len(primes)
if primes:
    total = primes[0]
for st in range(length):
    while en < length and total < n:
        en += 1
        if en != length:
            total += primes[en]
    if total == n: 
        ans += 1
    if en == length:
        break
    total -= primes[st]

print(ans)