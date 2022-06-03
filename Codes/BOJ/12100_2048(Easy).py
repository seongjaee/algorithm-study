from copy import deepcopy
import sys
input = sys.stdin.readline

def r(matrix):
    new_matrix = deepcopy(matrix)
    for i in range(n):
        for j in range(n - 1, -1, -1):
            if new_matrix[i][j]:
                for k in range(j-1, -1, -1):
                    if new_matrix[i][k] == new_matrix[i][j]:
                        new_matrix[i][j] *= 2
                        new_matrix[i][k] = 0
                        break
                    elif new_matrix[i][k]:
                        temp = new_matrix[i][k]
                        new_matrix[i][k] = 0
                        new_matrix[i][j-1] = temp
                        break
            else:
                temp = []
                k = j
                while len(temp) < 2 and k >= 0:
                    if new_matrix[i][k]:
                        temp.append(k)
                    k -= 1
                if len(temp) == 1:
                    new_matrix[i][j] = new_matrix[i][temp[0]]
                    new_matrix[i][temp[0]] = 0
                elif len(temp) == 2:
                    if new_matrix[i][temp[0]] == new_matrix[i][temp[1]]:
                        new_matrix[i][j] = 2 * new_matrix[i][temp[0]]
                        new_matrix[i][temp[0]] = 0
                        new_matrix[i][temp[1]] = 0
                    else:
                        new_matrix[i][j], new_matrix[i][temp[0]] = new_matrix[i][temp[0]], new_matrix[i][j]
                        new_matrix[i][j-1], new_matrix[i][temp[1]] = new_matrix[i][temp[1]], new_matrix[i][j-1]

    return new_matrix

def l(matrix):
    new_matrix = deepcopy(matrix)
    for i in range(n):
        for j in range(n):
            if new_matrix[i][j]:
                for k in range(j+1, n):
                    if new_matrix[i][k] == new_matrix[i][j]:
                        new_matrix[i][j] *= 2
                        new_matrix[i][k] = 0
                        break
                    elif new_matrix[i][k]:
                        temp = new_matrix[i][k]
                        new_matrix[i][k] = 0
                        new_matrix[i][j+1] = temp
                        break
            else:
                temp = []
                k = j
                while len(temp) < 2 and k < n:
                    if new_matrix[i][k]:
                        temp.append(k)
                    k += 1
                if len(temp) == 1:
                    new_matrix[i][j] = new_matrix[i][temp[0]]
                    new_matrix[i][temp[0]] = 0
                elif len(temp) == 2:
                    if new_matrix[i][temp[0]] == new_matrix[i][temp[1]]:
                        new_matrix[i][j] = 2 * new_matrix[i][temp[0]]
                        new_matrix[i][temp[0]] = 0
                        new_matrix[i][temp[1]] = 0
                    else:
                        new_matrix[i][j], new_matrix[i][temp[0]] = new_matrix[i][temp[0]], new_matrix[i][j]
                        new_matrix[i][j+1], new_matrix[i][temp[1]] = new_matrix[i][temp[1]], new_matrix[i][j+1]



    return new_matrix

def d(matrix):
    new_matrix = deepcopy(matrix)

    for j in range(n):
        for i in range(n-1, -1, -1):
            if new_matrix[i][j]:
                for k in range(i-1, -1, -1):
                    if new_matrix[k][j] == new_matrix[i][j]:
                        new_matrix[i][j] *= 2
                        new_matrix[k][j] = 0
                        break
                    elif new_matrix[k][j]:
                        temp = new_matrix[k][j]
                        new_matrix[k][j] = 0
                        new_matrix[i-1][j] = temp
                        break
            else:
                temp = []
                k = i
                while len(temp) < 2 and k >= 0:
                    if new_matrix[k][j]:
                        temp.append(k)
                    k -= 1
                if len(temp) == 1:
                    new_matrix[i][j] = new_matrix[temp[0]][j]
                    new_matrix[temp[0]][j] = 0
                elif len(temp) == 2:
                    if new_matrix[temp[0]][j] == new_matrix[temp[1]][j]:
                        new_matrix[i][j] = 2 * new_matrix[temp[0]][j]
                        new_matrix[temp[0]][j] = 0
                        new_matrix[temp[1]][j] = 0
                    else:
                        new_matrix[i][j], new_matrix[temp[0]][j] = new_matrix[temp[0]][j], new_matrix[i][j]
                        new_matrix[i-1][j], new_matrix[temp[1]][j] = new_matrix[temp[1]][j], new_matrix[i-1][j]
                        
    return new_matrix

def u(matrix):
    new_matrix = deepcopy(matrix)

    for j in range(n):
        for i in range(n):
            if new_matrix[i][j]:
                for k in range(i+1, n):
                    if new_matrix[k][j] == new_matrix[i][j]:
                        new_matrix[i][j] *= 2
                        new_matrix[k][j] = 0
                        break
                    elif new_matrix[k][j]:
                        temp = new_matrix[k][j]
                        new_matrix[k][j] = 0
                        new_matrix[i+1][j] = temp
                        break
            else:
                temp = []
                k = i
                while len(temp) < 2 and k < n:
                    if new_matrix[k][j]:
                        temp.append(k)
                    k += 1
                if len(temp) == 1:
                    new_matrix[i][j] = new_matrix[temp[0]][j]
                    new_matrix[temp[0]][j] = 0
                elif len(temp) == 2:
                    if new_matrix[temp[0]][j] == new_matrix[temp[1]][j]:
                        new_matrix[i][j] = 2 * new_matrix[temp[0]][j]
                        new_matrix[temp[0]][j] = 0
                        new_matrix[temp[1]][j] = 0
                    else:
                        new_matrix[i][j], new_matrix[temp[0]][j] = new_matrix[temp[0]][j], new_matrix[i][j]
                        new_matrix[i+1][j], new_matrix[temp[1]][j] = new_matrix[temp[1]][j], new_matrix[i+1][j]

    return new_matrix

def dfs(matrix, cnt):
    global max_value
    if cnt == 5:
        for row in matrix:
            for num in row:
                if num > max_value:
                    max_value = num
        # print(matrix)
        return
        

    for f in [r, l, d, u]:
        dfs(f(matrix), cnt + 1)

n = int(input())
matrix = [[*map(int, input().split())] for _ in range(n)]

max_value = 0
dfs(matrix, 0)
print(max_value)
# print(l(matrix))

f = {'r': r, 'l': l, 'u': u, 'd': d}

# while True:
#     cmd = input().rstrip()
#     print(f[cmd](matrix))
#     # print(matrix)
