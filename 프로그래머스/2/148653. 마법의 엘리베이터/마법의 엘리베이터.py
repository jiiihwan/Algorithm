def solution(storey):
    ans = 0
    
    while storey > 0:
        digit = storey % 10 
        next_digit = (storey % 100) // 10
        if digit >= 6:
            storey += 10 - digit
            ans += 10 - digit
        elif digit <= 4:
            storey -= digit
            ans += digit
        else: #5일때
            if next_digit >= 5:
                storey += 5
                ans += 5
            else:
                storey -= 5
                ans += 5
        
        storey //= 10
        
    
    return ans