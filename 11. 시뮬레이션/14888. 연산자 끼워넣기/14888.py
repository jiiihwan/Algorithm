import sys
input = sys.stdin.readline

N = int(input())
A = [list(map(int,input().split()))]
operators = list(map(int,input().split())) #+,-,*,//

max_ans = -1000000000
min_ans = 1000000000

def calculate(result):
    global max_ans
    global min_ans
    if spent_all:
        max_ans = max(max_ans, result)
        min_ans = min(min_ans, result)
        return
    for num in A:
        if 
        calculate(result)