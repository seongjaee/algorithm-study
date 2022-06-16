def convertTime2Sec(time):
    hour, minute, second = map(int, time.split(":"))
    return 3600 * hour + 60 * minute + second


def convertSec2Time(sec):
    hour = sec // 3600
    minute = (sec - hour * 3600) // 60
    second = sec % 60
    return f"{hour:02}:{minute:02}:{second:02}"


def solution(play_time, adv_time, logs):
    play_time = convertTime2Sec(play_time)
    adv_time = convertTime2Sec(adv_time)
    times = [tuple(map(convertTime2Sec, log.split("-"))) for log in logs]

    n = play_time + 1

    counter = [0] * (n + 1)
    for start, end in times:
        counter[start + 1] += 1
        counter[end + 1] -= 1

    for i in range(1, n + 1):
        counter[i] += counter[i - 1]

    for i in range(1, n + 1):
        counter[i] += counter[i - 1]

    max_value = 0
    max_start = []

    for s in range(0, n):
        if s + adv_time >= n:
            break
        if counter[s + adv_time] - counter[s] > max_value:
            max_value = counter[s + adv_time] - counter[s]
            max_start = [s]
        elif counter[s + adv_time] - counter[s] == max_value:
            max_start.append(s)

    result = list(map(convertSec2Time, sorted(max_start)))
    answer = result[0]

    return answer
