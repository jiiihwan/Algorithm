T = int(input())
for test_case in range(1, T + 1):
    pattern = input()
    ans = 11
    for n in range(1,11):
        temp = set()
        i = 0
        while i < n * (30 // n):
            temp.add(pattern[i:i+n])
            i += n
        if len(temp) == 1:
            ans = min(ans,n)

    print(f"#{test_case} {ans}")