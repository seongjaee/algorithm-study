from collections import deque
import sys
input = sys.stdin.readline

def topology_sort():
    queue = deque([])
    result = []

    for i in range(1, n + 1):
        if degrees[i] == 0:
            queue.append(i)
    
    while queue:
        now = queue.popleft()
        result.append(now)
        
        for nxt in graph.get(now, []):
            degrees[nxt] -= 1

            if degrees[nxt] == 0:
                queue.append(nxt)

    return result


n, m = map(int, input().split())

graph = {}
degrees = [0] * (n + 1)
for _ in range(m):
    _, *input_line = list(map(int, input().split()))
    for idx, value in enumerate(input_line):
        if idx == len(input_line) - 1:
            break
        graph[value] = graph.get(value, []) + [input_line[idx + 1]]
        degrees[input_line[idx + 1]] += 1

result = topology_sort()
if len(result) != n:
    print(0)
else:
    for num in result:
        print(num)