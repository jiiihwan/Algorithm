L = int(input())
ch = list(input())
for i in range(L):
    ch[i] = ord(ch[i]) - ord('a') + 1

H = 0
r = 1
for i in range(L):
    H = (H + (ch[i] * (31**i)%1234567891)) % 1234567891 
print(H)