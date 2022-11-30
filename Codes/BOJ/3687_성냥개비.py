import sys

input = sys.stdin.readline


MATCH_NUM = {2: [1], 3: [7], 4: [4], 5: [2, 3, 5], 6: [0, 6, 9], 7: [8]}

memo = [["", ""], ["", ""], [1, 1], [7, 7], [4, 11]]

for i in range(5, 101):
    min_value = int(1e51)
    max_value = -1
    for num, matches in MATCH_NUM.items():
        if i - num == 1 or i - num < 0:
            continue
        prev_min, prev_max = memo[i - num]
        numbers = []
        for match in matches:
            numbers.append(f"{prev_min}{match}")
            numbers.append(f"{prev_max}{match}")
            if match == 0:
                continue
            numbers.append(f"{match}{prev_min}")
            numbers.append(f"{match}{prev_max}")

        for str_number in numbers:
            if str_number[0] == "0":
                continue
            min_value = min(min_value, int(str_number))
            max_value = max(max_value, int(str_number))

    memo.append([min_value, max_value])


t = int(input())
for _ in range(t):
    n = int(input())
    print(*memo[n])
