def solution(dartResult):
    def S():
        return

    def D():
        score[-1] **= 2

    def T():
        score[-1] **= 3

    def star():
        score[-1] *= 2
        if len(score) > 1:
            score[-2] *= 2

    def acha():
        score[-1] *= -1

    bonus_option = {"S": S, "D": D, "T": T, "*": star, "#": acha}
    score = []
    number = ""

    for char in dartResult:
        if char.isdigit():
            number += char
        else:
            if number:
                score.append(int(number))
                number = ""
            bonus_option[char]()

    return sum(score)
