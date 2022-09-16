a, b = map (int, input().split())
m = int(input())
numbers = list(map(int, input().split()))

decimal = 0
for i, num in enumerate(numbers):
    decimal += (a ** (m-1-i)) * num
	
answer = []
while decimal:
    q, r = divmod(decimal, b)
    answer.append(r)
    decimal = q

print(*answer[::-1])
