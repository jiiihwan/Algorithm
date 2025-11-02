import sys
input = sys.stdin.readline

arr = []

N = int(input())
for _ in range(N):
    homework = input()
    temp = ''
    for i in homework:
        if not i.isdigit(): #문자일경우, 마지막에 개행문자도 걸린다.
            if temp != '':
                arr.append(int(temp))
                temp = ''
        else: #숫자일 경우 
            temp += i

arr.sort()
for i in arr:
    print(i)