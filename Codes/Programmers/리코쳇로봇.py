from collections import deque

def solution(board):
    DELTA = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    
    def find_point(target):
        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if char == target:
                    return (i, j)
                
    def is_reachable(y, x):
        if y < 0 or x < 0 or y >= n or x >= m:
            return False
        if board[y][x] == 'D':
            return False
        return True
                
    def get_reach_point(y, x, di):
        dy, dx = DELTA[di]
        while True:
            ny, nx = y + dy, x + dx
            if not is_reachable(ny, nx):
                return y, x
            y, x = ny, nx
        
    def bfs():
        visited = [[False] * m for _ in range(n)]
        visited[sy][sx] = True
        queue = deque([(sy, sx, 0)])
        
        while queue:
            y, x, cnt = queue.popleft()
            if board[y][x] == 'G':
                return cnt
            
            for di in range(4):
                ny, nx = get_reach_point(y, x, di)
                if visited[ny][nx]:
                    continue
                visited[ny][nx] = True
                queue.append((ny, nx, cnt + 1))
                
        return -1
        
        
    n = len(board)
    m = len(board[0])
    sy, sx = find_point('R')
    
    return bfs()