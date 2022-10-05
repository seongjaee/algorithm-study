import sys

input = sys.stdin.readline


while True:
    n = int(input())
    if n == 0:
        break

    next_rooms = [[] for _ in range(n + 1)]
    types = [""] * (n + 1)
    prices = [0] * (n + 1)

    for i in range(1, n + 1):
        row = input().split()
        room_type = row[0]
        price = int(row[1])
        nexts = list(map(int, row[2:-1]))

        types[i] = room_type
        prices[i] = price
        next_rooms[i] = nexts

    visited = [[False] * 501 for _ in range(n + 1)]
    visited[0][0] = True
    next_rooms[0] = [1]
    stack = [(0, 0)]
    while stack:
        room, money = stack.pop()
        if room == n:
            print("Yes")
            break

        for nxt_room in next_rooms[room]:
            if types[nxt_room] == "L":
                nxt_money = max(money, prices[nxt_room])

            elif types[nxt_room] == "T":
                nxt_money = money - prices[nxt_room]

            else:
                nxt_money = money

            if nxt_money < 0 or visited[nxt_room][nxt_money]:
                continue

            visited[nxt_room][nxt_money] = True
            stack.append((nxt_room, nxt_money))

    else:
        print("No")
