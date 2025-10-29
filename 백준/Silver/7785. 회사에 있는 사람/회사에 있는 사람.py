dic = {}

n = int(input())
for _ in range(n):
    name,log = input().split()
    dic[name] = log
    if log == 'leave':
        del dic[name]

dic = sorted(dic, reverse = True) # 기본값은 key기준 정렬

for k in dic:
    print(k)
