from collections import deque
import sys

input = sys.stdin.readline


def test():
    def roll():
        safety_numbers.appendleft(safety_numbers.pop())
        if is_on_person[n - 1]:
            is_on_person[n - 1] = False
        is_on_person.appendleft(is_on_person.pop())

    def walk():
        for i in range(n - 1, -1, -1):
            if not is_on_person[i]:
                continue
            if i == n - 1:
                is_on_person[i] = False
                continue
            if not is_on_person[i + 1] and safety_numbers[i + 1] > 0:
                is_on_person[i] = False
                is_on_person[i + 1] = True
                safety_numbers[i + 1] -= 1

    def get_on():
        if is_on_person[0] or safety_numbers[0] == 0:
            return
        is_on_person[0] = True
        safety_numbers[0] -= 1

    roll()
    walk()
    get_on()

    zero_cnt = 0
    for num in safety_numbers:
        if num == 0:
            zero_cnt += 1
    if zero_cnt >= k:
        return True

    return False


n, k = map(int, input().split())
safety_numbers = deque([*map(int, input().split())])
is_on_person = deque([False] * (2 * n))

is_end = False
answer = 0
while not is_end:
    answer += 1
    is_end = test()


print(answer)
