from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    orders = [sorted(order) for order in orders]

    for num in course:
        counter = {}
        for order in orders:
            comb = combinations(order, num)
            for menu in comb:
                counter[menu] = counter.get(menu, 0) + 1

        max_cnt = 2
        for menu, cnt in Counter(counter).most_common():
            max_cnt = max(max_cnt, cnt)
            if cnt >= max_cnt:
                answer.append("".join(menu))
            else:
                break
    answer.sort()

    return answer
