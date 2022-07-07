def dist(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def solution(numbers, hand):
    answer = ""

    locations = {0: (3, 1)}
    for i in range(1, 10):
        q, r = divmod(i - 1, 3)
        locations[i] = (q, r)

    left, right = (3, 0), (3, 2)

    left_col = {1, 4, 7}
    right_col = {3, 6, 9}

    for num in numbers:
        if num in left_col:
            answer += "L"
            left = locations[num]
        elif num in right_col:
            answer += "R"
            right = locations[num]
        else:
            if dist(left, locations[num]) > dist(right, locations[num]):
                answer += "R"
                right = locations[num]
            elif dist(left, locations[num]) < dist(right, locations[num]):
                answer += "L"
                left = locations[num]
            elif hand == "left":
                answer += "L"
                left = locations[num]
            else:
                answer += "R"
                right = locations[num]

    return answer
