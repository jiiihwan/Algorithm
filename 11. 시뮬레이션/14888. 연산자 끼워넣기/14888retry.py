import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
operators = list(map(int,input().split())) #+,-,*,//

max_ans = -float('inf')
min_ans = float('inf')

def calculate(idx,result):
    global max_ans,min_ans
    if idx == N:
        max_ans = max(max_ans, result)
        min_ans = min(min_ans, result)
        return
    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            if i == 0: #'+'
                calculate(idx+1, result+A[idx])
            elif i == 1: #'-'
                calculate(idx+1, result-A[idx])
            elif i == 2: #'*'
                calculate(idx+1, result*A[idx])
            else: # '//'
                if result < 0:
                    calculate(idx+1, -(-result//A[idx]))
                else:
                    calculate(idx+1, result//A[idx])
            operators[i] += 1

calculate(1,A[0])

print(max_ans)
print(min_ans)