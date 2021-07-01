def find(index):
    # index의 루트노드를 재귀적으로 찾음
    if parent[index] == index: 
        return index
    parent[index] = find(parent[index])
    return parent[index]

def union(x, y):
    # x와 y를 같은 집합으로
    x = find(x)
    y = find(y)

    if x== y:
        return

    if parent[x] > parent[y]:
        parent[x] = y
    else:
        parent[y] = x


n = 10
parent = [i for i in range(n)]

union(0,2)
union(2,3)
union(4,5)
union(5,6)
union(7,8)
union(9,7)

print(parent) # [0, 1, 0, 0, 4, 4, 4, 7, 7, 7]
