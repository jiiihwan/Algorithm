import sys
input = sys.stdin.readline

N = int(input())
tshirts = list(map(int,input().split()))
T,P = map(int, input().split())

T_ans = 0
for t in tshirts:
    if t % T == 0:
        T_ans += t // T
    else:
        T_ans += t // T + 1
print(T_ans)
print(N//P, N%P)