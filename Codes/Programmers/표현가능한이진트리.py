from math import log2, ceil


def convert(number):
    binary = f"{number:b}"
    k = len(binary)
    log = log2(k + 1)
    max_length = 2 ** ceil(log) - 1
    return "0" * (max_length - k) + binary


def check(bin_num):
    k = len(bin_num)
    root = bin_num[k // 2]
    if k == 1:
        return root, True

    left_root, left_check = check(bin_num[: k // 2])
    right_root, right_check = check(bin_num[k // 2 + 1 :])
    if not left_check or not right_check:
        return root, False
    if bin_num[k // 2] == "0" and (left_root == "1" or right_root == "1"):
        return root, False
    return root, True


def solution(numbers):
    answer = []
    for num in numbers:
        _, result = check(convert(num))
        answer.append(1 if result else 0)
    return answer


solution([5, 7, 42, 63, 95, 111])
