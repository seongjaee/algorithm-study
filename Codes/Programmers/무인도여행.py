def solution(maps):
    DELTA = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    def dfs(sy, sx):
        stack = [(sy, sx)]
        visited[sy][sx] = True
        result = int(maps[sy][sx])
        while stack:
            y, x = stack.pop()
            for dy, dx in DELTA:
                ny, nx = dy + y, dx + x
                if ny < 0 or ny >= n or nx < 0 or nx >= m:
                    continue
                if visited[ny][nx] or maps[ny][nx] == 'X':
                    continue
                visited[ny][nx] = True
                result += int(maps[ny][nx])
                stack.append((ny, nx))
        return result
    
    answer = []
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if visited[i][j] or maps[i][j] == 'X':
                continue
            answer.append(dfs(i, j))
            
    return sorted(answer) if answer else [-1]