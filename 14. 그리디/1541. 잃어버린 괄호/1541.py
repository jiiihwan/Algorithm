import sys
input = sys.stdin.readline

tmp, sum = 0 , 0
is_minus = False

arr = input()

for i in range(len(arr)-1):
    if arr[i] == '-':
        if is_minus:
            sum -= tmp
        else:
            is_minus = True
            sum += tmp
        tmp = 0
    elif arr[i] == '+':
        if is_minus:
            sum -= tmp
        else:
            sum += tmp
        tmp = 0
    else:
        if tmp != 0:
            tmp *= 10
        tmp += int(arr[i])
        if i == len(arr)-2: #마지막 예외처리
            if is_minus:
                sum -= tmp  
            else:
                sum += tmp

print(sum)