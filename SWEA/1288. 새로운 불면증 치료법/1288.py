T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    allnum = {1,2,3,4,5,6,7,8,9,0}
    
    k = 1
    tmp = set()

    
    while tmp != allnum:
        n = N * k 
        x = n
        if x == 0:
            tmp.add(0)
        else:
            while x > 0:
                tmp.add(x % 10)
                x //= 10
        k += 1
    
    ans = n
    print(f"#{test_case} {ans}")