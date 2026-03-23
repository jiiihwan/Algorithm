from collections import deque

def solution(priorities, location):
    q = deque()
    mx = max(priorities) #현재 가장 높은 우선순위 기록
    for i,p in enumerate(priorities):
        q.append((i,p))
    print(q)
    
    cnt = 0
    while True:
        cur_process, cur_priorities = q.popleft()
        if mx > cur_priorities: #우선순위가 더 높은 프로세스가 있다면
            q.append((cur_process, cur_priorities))
        else:
            if q: #큐가 비어있지 않을때
                tmpq = [p for i,p in q]
                mx = max(tmpq)
                cnt += 1
                if location == cur_process:
                    return cnt
            else:
                return len(priorities)