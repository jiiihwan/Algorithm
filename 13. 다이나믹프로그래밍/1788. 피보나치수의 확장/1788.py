n = int(input())

F = [0] * (abs(n)+1)
if abs(n) >= 1:
    F[1] = 1
for i in range(2,abs(n)+1):
    F[i] = (F[i-1] + F[i-2]) % 1000000000

if n == 0:
    print(0)
elif n < 0 and abs(n) % 2 == 0: #짝수이면
    print(-1)
else:
    print(1)
print(F[abs(n)])