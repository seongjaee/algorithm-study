def time_parser(end_time):
    result = 0
    h, m, s = end_time.split(":")
    result += int(h) * 3600000
    result += int(m) * 60000
    result += int(float(s) * 1000)
    return result


def solution(lines):
    answer = 0
    lines.sort()
    time_line = []
    for line in lines:
        _, end, time = line.split()
        time = int(float(time[:-1]) * 1000)
        end_time = time_parser(end)
        time_line.append((end_time - time + 1, end_time))

    max_value = 1
    i = 1
    for i in range(len(time_line)):
        st, et = time_line[i]
        s_right = st + 999
        e_right = et + 999
        s_cnt = 0
        e_cnt = 0
        for j in range(len(time_line)):
            nst, net = time_line[j]
            if (
                (st <= nst <= s_right)
                or (st <= net <= s_right)
                or (nst <= st <= s_right <= net)
            ):
                s_cnt += 1
            if (
                (et <= nst <= e_right)
                or (et <= net <= e_right)
                or (nst <= et <= e_right < net)
            ):
                e_cnt += 1

        max_value = max([max_value, s_cnt, e_cnt])

    return max_value
