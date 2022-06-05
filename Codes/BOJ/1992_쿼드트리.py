import sys
input = sys.stdin.readline

def check(r, c, size):
    result = 0
    for i in range(r, r+size):
        for j in range(c, c+size):
            result += matrix[i][j]
    if result == 0:
        return 0
    elif result == size ** 2:
        return 1
    else:
        return -1

def quad_tree(r, c, size):
    global answer
    
    result = check(r, c, size)
    if result != -1:
        answer += f'{result}'
    else:
        answer += '('
        quad_tree(r, c, size // 2)
        quad_tree(r, c + size // 2, size // 2)
        quad_tree(r + size // 2, c, size // 2)
        quad_tree(r + size // 2, c + size // 2, size // 2)
        answer += ')'

n = int(input())
matrix = [[*map(int, list(input().rstrip()))] for _ in range(n)]
answer = ''
quad_tree(0, 0, n)
print(answer)