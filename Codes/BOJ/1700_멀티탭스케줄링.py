import sys

input = sys.stdin.readline

answer = 0
n, k = map(int, input().split())
plug_numbers = [*map(int, input().split())]

on_plugs = set()
# 첫 n개를 우선 꽂는다
for i in range(n):
    on_plugs.add(plug_numbers[i])

for i in range(n, k):
    curr_plug = plug_numbers[i]
    # 이미 사용 중이면 건너뜀
    if curr_plug in on_plugs:
        continue

    # 아직 빈 공간이 있으면 꽂음
    if len(on_plugs) < n:
        on_plugs.add(curr_plug)
        continue

    # 이미 사용 중인 플러그들의 가장 가까운 사용 시기
    near_index = [1000] * (k + 1)
    for j in range(k - 1, i, -1):
        plug = plug_numbers[j]
        if plug in on_plugs:
            near_index[plug] = j

    # 가장 나중에 쓰이게 될 플러그
    most_later_plug = 0
    most_later_index = 0
    for plug in on_plugs:
        if near_index[plug] > most_later_index:
            most_later_plug = plug
            most_later_index = near_index[plug]
        if near_index[plug] == 1000:
            break

    on_plugs.remove(most_later_plug)
    on_plugs.add(curr_plug)

    answer += 1

print(answer)
