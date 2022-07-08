def convert_sharp2lower(scores):
    result = []
    for score in scores:
        if score == "#":
            result.append(result.pop().lower())
        else:
            result.append(score)
    return "".join(result)


def played_time(start, end):
    sh, sm = map(int, start.split(":"))
    eh, em = map(int, end.split(":"))
    return (eh - sh) * 60 + (em - sm)


def played_melody(start, end, score):
    total_time = played_time(start, end)
    k = len(score)
    q, r = divmod(total_time, k)
    return score * q + score[:r]


def solution(m, musicinfos):
    m = convert_sharp2lower(m)
    result = []
    for musicinfo in musicinfos:
        start, end, name, score = musicinfo.split(",")
        melody = played_melody(start, end, convert_sharp2lower(score))
        if m in melody:
            result.append((name, played_time(start, end)))

    if result:
        result.sort(key=lambda x: -x[1])
        return result[0][0]
    else:
        return "(None)"
