def solution(brown, yellow):
    for i in range(1,yellow+1):
        if yellow % i == 0:
            j = yellow//i
            y,x = i+2, j+2
            if x*y - brown == yellow:
                ans = [x,y]
                return ans
        else:
            continue

    