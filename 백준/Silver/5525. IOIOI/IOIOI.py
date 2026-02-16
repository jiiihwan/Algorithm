import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = list(input())

P = ['I','O','I'] #P1
for _ in range(1,N):
    P.append('O')
    P.append('I')

ans = 0
for i in range(M-2*N):
    for j in range(len(P)):
        if S[i+j] != P[j]:
            break
    else:
        ans += 1

print(ans)