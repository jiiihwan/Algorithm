import sys
input = sys.stdin.readline

f = [[0,0] for _ in range(41)]  #0-based index
f[0] = [1,0]
f[1] = [0,1]

for i in range(2,41):
    f[i][0] = f[i-1][0] + f[i-2][0]
    f[i][1] = f[i-1][1] + f[i-2][1]

T = int(input())
for _ in range(T):
    N = int(input())
    print(f[N][0], f[N][1])

'''
코테 재활 1일차
입력받을때 int쓰는거랑
리스트 초기화할때 *말고 리스트 컴프리헨션으로 쓰기 까먹지 말기!!
'''