def make_counter(string):
    result = {}
    for i in range(len(string) - 1):
        now = string[i] + string[i + 1]
        if now.isalpha():
            result[now] = result.get(now, 0) + 1
    return result


def jaccard(counter1, counter2):
    if len(counter1) + len(counter2) == 0:
        return 1
    inter = 0
    union = {}
    for key, value in counter1.items():
        inter += min(value, counter2.get(key, 0))
        union[key] = max(value, counter2.get(key, 0))

    for key, value in counter2.items():
        union[key] = max(value, counter1.get(key, 0))

    return inter / sum(union.values())


def solution(str1, str2):
    counter1 = make_counter(str1.lower())
    counter2 = make_counter(str2.lower())

    return int(jaccard(counter1, counter2) * 65536)
