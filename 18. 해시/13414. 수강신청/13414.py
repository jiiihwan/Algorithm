import sys
input = sys.stdin.readline

dic = {}

K,L = map(int, input().split())
for i in range(L):
    a = input().rstrip()
    dic[a] = i

dic = sorted(dic.items(), key = lambda x : x[1]) #dic은 이제 리스트안에 튜플을 원소로 가지는 형태가 된다

for i in range(K):
    if i < len(dic):
        print(dic[i][0]) #튜플의 첫번째 원소(학번) 출력
    else:
        break