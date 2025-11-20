T = int(input())

for test_case in range(1, T + 1):
    word = input()
    ans = 0
    n = len(word)
    if n%2 == 1:
        if word[:n//2] == word[:n//2:-1]:
            ans = 1
    else:
        if word[:n//2] == word[:n//2-1:-1]:
            ans = 1

    print(f"#{test_case} {ans}")