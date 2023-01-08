import sys

input = sys.stdin.readline

# 1월 1일 => 1, 12월 31일 => 365
def date_to_num(month, day):
    result = day
    days_by_month = [0, 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    for m in range(1, month + 1):
        result += days_by_month[m]
    return result


n = int(input())


flowers_life_date = []
for _ in range(n):
    sm, sd, em, ed = map(int, input().split())
    start = date_to_num(sm, sd)
    end = date_to_num(em, ed)
    flowers_life_date.append((start, end))

flowers_life_date.sort(key=lambda tup: (tup[0], tup[1]))
now = date_to_num(3, 1)
goal = date_to_num(11, 30)

i = 0
answer = 0
while i < n:
    if now >= goal + 1:
        break
    last_index = i
    last_day = now
    for idx, (s, e) in enumerate(flowers_life_date[i:]):
        if now < s:
            break
        last_index = idx
        last_day = max(last_day, e)

    if now == last_day:
        answer = 0
        break

    now = last_day
    i = last_index + 1
    answer += 1

if now <= goal:
    answer = 0

print(answer)
"""
현재 날짜보다 이전에 피기 시작해서, 가장 오랫동안 피는 꽃
(s, e) such as s <= now, max(e)
"""
