def sort_key(file):
    head = ""
    for idx, char in enumerate(file):
        if char.isdigit():
            break
        head += char

    number = ""
    for i in range(idx, len(file)):
        if i == idx + 5 or not file[i].isdigit():
            break
        number += file[i]

    return (head.lower(), int(number))


def solution(files):
    files.sort(key=sort_key)
    return files
