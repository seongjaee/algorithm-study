import sys
input = sys.stdin.readline

def cross_product(v, w):
    x1, y1 = v
    x2, y2 = w
    return x1 * y2 - x2 * y1

def get_vector(start, end):
    return (end[0] - start[0], end[1] - start[1])


n = int(input())

points = [tuple(map(int, input().split())) for _ in range(n)]
vectors = []

for point in points[1:]:
    vectors.append(get_vector(points[0], point))

areas = 0
for idx, vector in enumerate(vectors):
    if idx == 0:
        continue
    
    areas += cross_product(vectors[idx - 1], vector) * 0.5

print(abs(areas))