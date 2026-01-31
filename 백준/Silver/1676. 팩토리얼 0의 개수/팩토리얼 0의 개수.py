N = int(input())
fac = 1
for i in range(1,N+1):
    fac *= i

ans = 0
while fac % 10 == 0:
    fac //= 10
    ans += 1

print(ans)