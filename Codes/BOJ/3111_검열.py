from collections import deque
import sys

input = sys.stdin.readline

A = input().rstrip()
reversed_A = list(reversed(A))
T = deque(input().rstrip())
n = len(A)


def algorithm(T):
    left = []
    right = []
    while T:
        # 앞에서 찾기
        while True:
            if left[-n:] == list(A):
                left[-n:] = []
                break

            if not T:
                break

            left.append(T.popleft())

        # 뒤에서 찾기
        while True:
            if right[-n:] == reversed_A:
                right[-n:] = []
                break

            if not T:
                break

            right.append(T.pop())

    while right:
        if left[-n:] == list(A):
            left[-n:] = []

        left.append(right.pop())

    return left


answer = "".join(algorithm(T))
print(answer)
