def find_not_dwarf(arr):
    goal = sum(arr) - 100
    for i in range(8):
        for j in range(i + 1, 9):
            if heights[i] + heights[j] == goal:
                return i, j


heights = [int(input()) for _ in range(9)]
a, b = find_not_dwarf(heights)
answer = sorted([heights[i] for i in range(9) if i != a and i != b])
print("\n".join(map(str, answer)))
