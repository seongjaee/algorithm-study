from collections import deque
import sys

input = sys.stdin.readline


def solution(crains, boxes):
    if boxes[-1] > crains[0]:
        return -1
    result = 0
    while boxes:
        temp = deque()
        for crain in crains:
            while boxes:
                box = boxes.pop()
                if box > crain:
                    temp.appendleft(box)
                else:
                    break
        boxes += temp
        result += 1

    return result


n = int(input())
crains = list(map(int, input().split()))
m = int(input())

boxes = deque(sorted(map(int, input().split())))
crains.sort(reverse=True)

print(solution(crains, boxes))
