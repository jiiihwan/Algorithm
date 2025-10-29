import sys
input = sys.stdin.readline

N,M = map(int, input().split())

dic = {}
num = {}
for i in range(1,N+1):
    x = input().rstrip() #딕셔너리 쓸때는 rstrip() 꼭 해주기!!
    dic[i] = x
    num[x] = i

for j in range(M):
    a = input().rstrip()
    if a.isdigit():
        print(dic.get(int(a)))
    else:
        print(num.get(a))