from itertools import combinations


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
        for menu in sorted(counter.keys(), key=lambda x: -counter[x]):
            cnt = counter[menu]
            max_cnt = max(max_cnt, cnt)
            if cnt >= max_cnt:
                answer.append("".join(menu))
            else:
                break
    answer.sort()

    return answer


# 두번째 풀이
from itertools import combinations as cbnts


def solution(orders, course):
    orders = [sorted(order) for order in orders]
    answer = []
    for k in course:
        menus_counter = {}
        max_count = 2
        max_menus = []
        for order in orders:
            comb = list(cbnts(order, k))
            for menus in comb:
                menus_counter[menus] = menus_counter.get(menus, 0) + 1

                if max_count < menus_counter[menus]:
                    max_count = menus_counter[menus]
                    max_menus = ["".join(menus)]
                elif max_count == menus_counter[menus]:
                    max_menus.append("".join(menus))

        answer += max_menus

    answer.sort()

    return answer
