ISBN = list(input())
check = int(ISBN[12])
num = 0
for i in range(12):
    if ISBN[i] != '*':
        if i % 2 == 0:
            num += int(ISBN[i])
        else:
            num += 3 * int(ISBN[i])
    else:
        idx = i

ans = (10 - ((num+check)%10)) % 10

if idx % 2 == 1:
    ans = (ans * 7) % 10

print(ans)