def solution(s, skip, index):
    answer = ""
    remains = []

    for i in range(26):
        char = chr(i + ord("a"))
        if char not in skip:
            remains.append(char)

    n = len(remains)
    index_dict = {char: idx for idx, char in enumerate(remains)}
    for char in s:
        i = (index_dict[char] + index) % n
        answer += remains[i]

    return answer
