import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip() # 리스트 변환 없이 문자열 그대로 사용해도 충분

ans = 0
count = 0 # 연속된 'OI' 패턴의 개수
i = 1

# 문자열을 한 번만 순회 (O(M))
while i < M - 1:
    # 'IOI' 패턴 발견 시
    if S[i-1] == 'I' and S[i] == 'O' and S[i+1] == 'I':
        count += 1
        # 연속된 'OI'가 N개가 되면 PN 패턴 완성
        if count == N:
            ans += 1
            count -= 1 # 다음 'OI'가 붙으면 또 다른 PN이 될 수 있으므로 1만 줄임
        i += 2 # 'IOI'를 찾았으니 다음 'O'는 건너뛰고 'I' 위치부터 다시 확인
    else:
        count = 0 # 패턴이 깨지면 카운트 초기화
        i += 1

print(ans)