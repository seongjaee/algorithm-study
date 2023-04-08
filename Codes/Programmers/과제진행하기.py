def time_to_num(time):
    hh, mm = map(int, time.split(":"))
    return hh * 60 + mm


def solution(plans):
    answer = []
    remain_assigns = []
    remain_time = {}
    start_time = {}
    for name, start, time in plans:
        start = time_to_num(start)
        remain_time[name] = int(time)
        start_time[start] = name

    now_assign = ""
    for now_time in range(time_to_num("23:59") + 100000):
        if now_time in start_time:
            if now_assign:
                remain_assigns.append(now_assign)
            now_assign = start_time[now_time]

        if now_assign == "" and remain_assigns:
            now_assign = remain_assigns.pop()

        if now_assign:
            remain_time[now_assign] -= 1

            if remain_time[now_assign] == 0:
                answer.append(now_assign)
                now_assign = ""

    return answer
