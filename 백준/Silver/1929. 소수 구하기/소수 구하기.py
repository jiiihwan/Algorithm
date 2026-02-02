M,N = map(int, input().split())
is_prime = [True] * (N+1) #0-based index
is_prime[0] = is_prime[1] = False
for i in range(2, int(N**0.5) + 1): #제곱근까지만 본다
    if is_prime[i]:
        for j in range(i*i, N+1, i): #i의 배수는 모두 소수가 아니다
            is_prime[j] = False

for i in range(M,N+1):
    if is_prime[i]:
        print(i)