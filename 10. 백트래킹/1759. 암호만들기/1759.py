L,C = map(int,input().split())
alphabets = sorted(list(input().split()))
vowel = ['a','e','i','o','u']

cnt_vowel, cnt_else = 0,0
password = []

def make_password(start,depth):
    global cnt_vowel, cnt_else
    if cnt_vowel >= 1 and cnt_else >= 2 and depth == L:
        print(''.join(password))
        return
    for i in range(start, C):
        if alphabets[i] in vowel:
            cnt_vowel += 1
        else:
            cnt_else += 1
        password.append(alphabets[i])
        make_password(i+1,depth+1)
        password.pop()
        if alphabets[i] in vowel:
            cnt_vowel -= 1
        else:
            cnt_else -= 1

make_password(0,0)