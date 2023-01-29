from collections import deque

def solution(numbers):
    answer = []
    queue = deque()
    while numbers:
        flag = True
        num = numbers.pop()
        while queue:
            nxt = queue[0]
            if nxt > num:
                flag = False
                answer.append(nxt)
                break
            else:
                queue.popleft()
        if flag:
            answer.append(-1)
        queue.appendleft(num)

    return answer[::-1]