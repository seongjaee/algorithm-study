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


# 두번째 풀이
def hhmmss2time(hhmmss):
    hh, mm, ss = map(int, hhmmss.split(":"))
    return hh * 3600 + mm * 60 + ss


def time2hhmmss(time):
    hh, mmss = divmod(time, 3600)
    mm, ss = divmod(mmss, 60)
    return f"{hh:02}:{mm:02}:{ss:02}"


def solution(play_time, adv_time, logs):
    timestamp = [0] * (hhmmss2time(play_time) + 2)
    adv_time_long = hhmmss2time(adv_time)

    for log in logs:
        start_time, end_time = map(hhmmss2time, log.split("-"))
        timestamp[start_time] += 1
        timestamp[end_time] -= 1

    presum = [timestamp[0]]
    for i in range(1, len(timestamp)):
        presum.append(presum[-1] + timestamp[i])

    left = 0
    right = adv_time_long - 1
    window = sum(presum[left : right + 1])

    max_value = window
    max_idx = left
    while right < len(presum) - 1:
        window -= presum[left]
        window += presum[right + 1]
        left += 1
        right += 1
        if window > max_value:
            max_value = window
            max_idx = left

    return time2hhmmss(max_idx)
