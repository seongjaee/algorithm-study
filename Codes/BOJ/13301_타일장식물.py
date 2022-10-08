n = int(input())

fibo = [1, 1]
for _ in range(80):
    fibo.append(fibo[-2] + fibo[-1])

print(2 * (fibo[n - 1] + fibo[n]))
