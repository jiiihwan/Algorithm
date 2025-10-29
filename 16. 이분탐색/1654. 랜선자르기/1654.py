import sys
input = sys.stdin.readline

K,N = map(int, input().split())
lan = list(int(input()) for _ in range(K))

#랜선을 얼마만큼 자를건지 정하는 과정.
st, en = 1, max(lan) #자를수있는 범위지정
while st <= en:
    mid = (st+en)//2 #홀수로 나뉘면 버림
    cnt = 0 #몇개로 나뉘는지 세기 위함
    for i in lan:
        cnt += i//mid #모든 랜선을 mid만큼 잘랐을때 몇개 나뉘냐?
    if cnt >= N: #N개보다 더 많이 잘렸다면 덜 잘리도록, 길이가 늘어나도록 st를 옮겨서 더 큰 길이로 자르게 한다
        st = mid + 1
    else:
        end = mid - 1 #N개 보다 부족하다면 너무 크게 자른거니까 줄인다

#반복하다 보면 st가 en을 넘기면서 종료된다. 종료되기 직전 st와 en값 사이에 있는 것들이 
print(end)