def solution(survey, choices):
    answer = ""
    scores = {"R": 0, "C": 0, "J": 0, "A": 0}
    for indicators, score in zip(survey, choices):
        if indicators[0] in scores:
            scores[indicators[0]] -= score - 4
        else:
            scores[indicators[1]] += score - 4

    for key in ["RT", "CF", "JM", "AN"]:
        if scores[key[0]] >= 0:
            answer += key[0]
        else:
            answer += key[1]

    return answer
