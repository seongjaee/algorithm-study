def compare(user, banned):
    for i in range(len(user)):
        if banned[i] != "*" and user[i] != banned[i]:
            return False
    return True


def solution(user_id, banned_id):
    def brute_force(level, visited):
        if level == len(banned_id):
            result.add(visited)
            return

        for num in graph[level]:
            if not visited & (1 << num):
                brute_force(level + 1, visited | (1 << num))

    graph = [[] for _ in range(len(banned_id))]
    for i, ban in enumerate(banned_id):
        for j, user in enumerate(user_id):
            if len(user) == len(ban) and compare(user, ban):
                graph[i].append(j)

    result = set()

    brute_force(0, 0)

    return len(result)
