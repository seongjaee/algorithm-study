import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lights_table = [input().rstrip() for _ in range(n)]
k = int(input())

answer = 0
for i, lights in enumerate(lights_table):
    off_cnt = 0
    for char in lights:
        if char == "0":
            off_cnt += 1

    # 이 행은 켤 수 없음
    if off_cnt > k or (k % 2) != (off_cnt % 2):
        continue

    # 이 행을 켜려고 했을 때 같이 켜지는 행들의 수
    same_lights_cnt = 0
    for j in range(i, n):
        if lights == lights_table[j]:
            same_lights_cnt += 1
    answer = max(answer, same_lights_cnt)

print(answer)
