import sys

input = sys.stdin.readline

goal_size = int(input())
m, n = map(int, input().split())

pizza_a = [int(input()) for _ in range(m)]
pizza_b = [int(input()) for _ in range(n)]

pizza_a = pizza_a + pizza_a
pizza_b = pizza_b + pizza_b

presum_a = [0]
for i in range(2 * m):
    presum_a.append(presum_a[-1] + pizza_a[i])

presum_b = [0]
for i in range(2 * n):
    presum_b.append(presum_b[-1] + pizza_b[i])


def get_counter(presum):
    result = {0: 1, presum[len(presum) // 2]: 1}
    for i in range(len(presum) // 2):
        for j in range(i + 1, len(presum)):
            if j - i >= len(presum) // 2:
                break
            size = presum[j] - presum[i]
            if size <= goal_size:
                result[size] = result.get(size, 0) + 1
    return result


counter_a = get_counter(presum_a)
counter_b = get_counter(presum_b)

answer = 0
for size, count in counter_a.items():
    answer += counter_b.get(goal_size - size, 0) * count

print(answer)
