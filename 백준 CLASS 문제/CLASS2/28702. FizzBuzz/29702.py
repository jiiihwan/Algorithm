A = []
for i in range(3):
    A.append(input())

ans = 0
for i in range(3):
    if A[i].isdigit():
        ans = int(A[i]) + 3 - i

if ans % 3 == 0 and ans % 5 == 0:
    ans = "FizzBuzz"
elif ans % 3 == 0:
    ans = "Fizz"
elif ans % 5 == 0:
    ans = "Buzz"

print(ans)