def get_score(value):
    return 7 - value if value > 1 else 6


def solution(lottos, win_nums):
    min_value = len(set(lottos) & set(win_nums))
    max_value = min_value + lottos.count(0)

    return [*map(get_score, [max_value, min_value])]
