from collections import deque

n, k = map(int, input().split())


def solution(n, k):
    cnt = 0
    queue = deque(range(2, n + 1))
    while queue:
        num = queue.popleft()
        cnt += 1
        if k == cnt:
            return num

        for _ in range(len(queue)):
            temp = queue.popleft()
            if temp % num != 0:
                queue.append(temp)
            else:
                cnt += 1
                if k == cnt:
                    return temp


print(solution(n, k))
