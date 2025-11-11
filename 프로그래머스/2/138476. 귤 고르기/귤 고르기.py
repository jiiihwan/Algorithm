def solution(k, tangerine):
    tangerine.sort()
    num = []
    cnt = 1
    for i in range(1,len(tangerine)):
        if tangerine[i-1] == tangerine[i]:
            cnt += 1
        else:
            num.append(cnt)
            cnt = 1
    num.append(cnt) #마지막거도 추가해주기

    num.sort(reverse = True)
    for i,n in enumerate(num):
        k -= n
        if k <= 0:
            return i+1
        
        