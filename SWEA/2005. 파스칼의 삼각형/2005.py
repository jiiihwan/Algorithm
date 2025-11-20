T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    paskal = [[0,1,0]]
    for i in range(1,N):
        paskal.append([0])
        for j in range(1,i+2):
            paskal[i].append(paskal[i-1][j-1] + paskal[i-1][j])
        paskal[i].append(0)

    

    print(f"#{test_case}")
    for i in range(N):
        for j in paskal[i]:
            if j == 0:
                continue
            else:
                print(j, end=' ')
        print()     