def solution(want, number, discount):
    def is_match(counter):
        for item, num in zip(want, number):
            if counter.get(item, -1) != num:
                return False
        return True

    answer = 0
    counter = {}
    n = sum(number)
    for i in range(n):
        item = discount[i]
        counter[item] = counter.get(item, 0) + 1

    left, right = 0, n - 1

    while right < len(discount):
        if is_match(counter):
            answer += 1

        l_item = discount[left]
        counter[l_item] -= 1
        if counter[l_item] == 0:
            counter.pop(l_item)

        if right == len(discount) - 1:
            break

        r_item = discount[right + 1]
        counter[r_item] = counter.get(r_item, 0) + 1
        left += 1
        right += 1

    return answer
