from collections import deque

def bfs(num):
    queue = deque([(num, 1 << num)])
    visited = [False] * (num + 1)
    visited[num] = True
    
    while queue:
        now, path = queue.popleft()
        if now == 1:
            return path

        if now % 3 == 0:
            nxt = now // 3
            if not visited[nxt]:
                visited[nxt] = True
                queue.append((nxt, path | (1 << nxt)))

        if now % 2 == 0:
            nxt = now // 2
            if not visited[nxt]:
                visited[nxt] = True
                queue.append((nxt, path | (1 << nxt)))

        nxt = now - 1
        if not visited[nxt]:
            visited[nxt] = True
            queue.append((nxt, path | (1 << nxt)))


x = int(input())

result = f'{bfs(x):0b}'
answer = []
for idx, value in enumerate(result):
    if value == '1':
        answer.append(len(result) - idx - 1)

print(len(answer) - 1)
print(*answer)