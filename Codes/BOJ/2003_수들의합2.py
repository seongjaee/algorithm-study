n, m = map(int, input().split())

numbers = [*map(int, input().split())]

presum = [0]
for i in range(n):
    presum.append(presum[i] + numbers[i])

cnt = 0
left, right = 0, 1
while left <= right < n + 1:
    now = presum[right] - presum[left]
    if now == m:
        cnt += 1
        right += 1
        left += 1
    elif now > m:
        left += 1
    else:
        right += 1

print(cnt)
