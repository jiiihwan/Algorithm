def area(a,b): #y값을 넣는다
    return abs(a-b)/2 + min(a,b)

def solution(k, ranges):
    n = 0
    Collatz = [] #단계별 y좌표를 담는다
    while True:
        Collatz.append(k)
        if k == 1:
            break
        if k % 2 == 0:
            k //= 2
            n += 1
        else:
            k = k*3 + 1
            n += 1
    
    ans = []
    for a,b in ranges: #ranges를 순환
        cnt = 0
        if a > n+b:
            ans.append(-1)
            continue
        else:
            for i in range(a, n+b):
                cnt += area(Collatz[i],Collatz[i+1])
            ans.append(cnt)
    
    return ans