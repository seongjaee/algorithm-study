from collections import deque


def solution(queue1, queue2):
    max_count = len(queue1) * 4
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    left = sum(queue1)
    right = sum(queue2)
    cnt = 0
    while cnt < max_count:
        if left > right:
            num = queue1.popleft()
            left -= num
            right += num
            queue2.append(num)
        elif left < right:
            num = queue2.popleft()
            right -= num
            left += num
            queue1.append(num)
        else:
            break

        cnt += 1

    return cnt if cnt != max_count else -1
