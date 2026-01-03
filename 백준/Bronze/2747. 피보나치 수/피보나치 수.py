Fib = [0] * 46 #0-based index
Fib[1] = 1
for i in range(2,46):
    Fib[i] = Fib[i-1] + Fib[i-2]

n = int(input())
print(Fib[n])