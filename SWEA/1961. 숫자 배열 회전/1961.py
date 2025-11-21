T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    
    arr_90 = list(zip(*arr[::-1]))
    arr_180 = list(zip(*arr_90[::-1]))
    arr_270 = list(zip(*arr_180[::-1]))

    print(f"#{test_case}")
    for i in range(N):
        print(''.join(map(str,arr_90[i])), end = ' ')
        print(''.join(map(str,arr_180[i])), end = ' ')
        print(''.join(map(str,arr_270[i])), end = ' ')
        print()