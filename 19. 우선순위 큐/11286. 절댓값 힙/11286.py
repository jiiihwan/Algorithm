import sys, heapq
input = sys.stdin.readline

hq = [] #(절댓값, 실제값) 튜플을 이용해서 저장
N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        if not hq:
            print(0)
        else:
            #절댓값 작고 가장 작은수 출력
            #튜플을 비교할때는 첫째원소부터 자동으로 비교하니.. 우선순위는 절댓값이 같을때 실제값이 작은 순서대로다
            print(heapq.heappop(hq)[1])
    else:
        #hq에 우선순위 정해서 x담기
        heapq.heappush(hq, (abs(x), x))