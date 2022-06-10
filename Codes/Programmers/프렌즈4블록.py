from copy import deepcopy

def solution(m, n, b):
    
    def turn():
        nxt_board = deepcopy(board)
        flag2 = False  # 블록 지운게 있는지
        
        # 2x2 지우기
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                    
                # 2x2가 지워지는지 확인
                flag = True  
                for ny, nx in [(i+1, j), (i, j+1), (i+1, j+1)]:
                    if ny >= m or nx >= n:
                        flag = False
                        break
                    if board[ny][nx] != board[i][j]:
                        flag = False
                        break
                
                # 2x2 지우기
                if flag:
                    flag2 = True
                    nxt_board[i][j] = '.'
                    nxt_board[i+1][j] = '.'
                    nxt_board[i][j+1] = '.'
                    nxt_board[i+1][j+1] = '.'
                    
        # 블록 아래로 떨어트리기
        for j in range(n):
            for i in range(m-1, 0, -1):
                if nxt_board[i][j] != '.':
                    continue
                
                # 위에 블록 찾기
                flag3 = False
                for k in range(i-1, -1, -1):
                    if nxt_board[k][j] != '.':
                        flag3 = True
                        nxt_board[i][j], nxt_board[k][j] = nxt_board[k][j], nxt_board[i][j]
                        break

                # 위에 블록 없으면 그만
                if not flag3:
                    break                
                    
        return flag2, nxt_board
        
        
    answer = 0
    board = [list(row) for row in b]
    
    while True:        
        flag2, board = turn()
        if not flag2:
            break
            
    for i in range(m):
        for j in range(n):
            if board[i][j] == '.':
                answer += 1
    
    return answer