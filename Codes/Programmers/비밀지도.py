def convert2sharp(n, num):
    result = ""
    for x in f"{num:0{n}b}":
        result += "#" if x == "1" else " "
    return result


def solution(n, arr1, arr2):
    answer = []
    for x, y in zip(arr1, arr2):
        answer.append(convert2sharp(n, x | y))
    return answer
