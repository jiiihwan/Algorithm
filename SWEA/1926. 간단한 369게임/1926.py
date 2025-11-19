N = int(input())

ans = []
cond = ['3','6','9']

num = 0

while num < N:
    num += 1
    cnt = 0
    for a in str(num):
        if a in cond:
            cnt += 1
    if not cnt: #count가 0이 아닐때(369 아닐때)
        ans.append(str(num))
    else:
        ans.append("-"*cnt)

print(' '.join(ans))