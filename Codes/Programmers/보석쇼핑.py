def solution(gems):
    n = len(gems)
    total_cnt = len(set(gems))
    result = []
    left, right = 0, 0
    counter = {gems[0]: 1}

    while left <= right < n:
        if len(counter) == total_cnt:
            result.append([left + 1, right + 1])
            counter[gems[left]] -= 1
            if counter[gems[left]] == 0:
                counter.pop(gems[left])
            left += 1
        else:
            right += 1
            if right < n:
                counter[gems[right]] = counter.get(gems[right], 0) + 1

    result.sort(key=lambda arr: (arr[1] - arr[0], arr[0]))
    return result[0]
