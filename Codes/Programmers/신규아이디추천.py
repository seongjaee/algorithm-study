NOT_ALLOWED = "~!@#$%^&*()=+[{]}:?,<>/"


def solution(new_id: str):
    # level 1
    new_id = new_id.lower()

    # level 2
    for char in NOT_ALLOWED:
        new_id = new_id.replace(char, "")

    # level 3
    while True:
        if ".." not in new_id:
            break
        new_id = new_id.replace("..", ".")

    # level 4
    if new_id and new_id[0] == ".":
        new_id = new_id[1:]
    if new_id and new_id[-1] == ".":
        new_id = new_id[:-1]

    # level 5
    if not new_id:
        new_id = "a"

    # level 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]

    # level 7
    elif len(new_id) <= 2:
        new_id += new_id[-1] * (3 - len(new_id))

    return new_id
