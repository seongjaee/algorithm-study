import sys

sys.setrecursionlimit(100000)


def solution(name):
    # A로 바꾸는데 드는 비용
    def count2A(char):
        return min(ord(char) - 65, 91 - ord(char))

    # i: 현재 인덱스, cnt: 이동 횟수, A: A의 개수
    def dfs(i, cnt, A):
        nonlocal min_value
        if A == n:
            min_value = min(min_value, cnt)
            return
        # 가지치기
        if cnt >= min_value:
            return

        # 오른쪽으로 A 아닌 곳
        j = i
        while True:
            j += 1
            if not visited[j % n]:
                visited[j % n] = True
                dfs(j % n, cnt + j - i + count2A(name[j % n]), A + 1)
                visited[j % n] = False
                break

        # 왼쪽으로 A 아닌 곳
        j = i
        while True:
            j -= 1
            if not visited[j % n]:
                visited[j % n] = True
                dfs(j % n, cnt + i - j + count2A(name[j % n]), A + 1)
                visited[j % n] = False
                break

    n = len(name)
    visited = [False] * n  # A인가?
    a = 0
    for idx, char in enumerate(name):
        if char == "A":
            visited[idx] = True
            a += 1

    min_value = 1e10

    if name[0] == "A":
        dfs(0, 0, a)
    else:
        visited[0] = True
        dfs(0, count2A(name[0]), a + 1)

    return min_value
