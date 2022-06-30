from heapq import heappop, heappush


def hhmm2int(hhmm):
    h, m = map(int, hhmm.split(":"))
    return h * 60 + m


def int2hhmm(num):
    h, m = divmod(num, 60)
    return f"{h:02}:{m:02}"


def solution(n, t, m, timetable):
    time_line = []
    for time in timetable:
        heappush(time_line, hhmm2int(time))

    bus_times = [hhmm2int("09:00") + (i * t) for i in range(n)]
    bus_on_time = {}  # 시각: [탑승한 승객들의 도착 시각]
    for bus_time in bus_times:
        passengers = []
        while time_line and len(passengers) < m:
            if time_line[0] <= bus_time:
                passengers.append(heappop(time_line))
            else:
                break
        bus_on_time[bus_time] = passengers

    # 막차 탑승 정보
    last_bus = bus_on_time[bus_times[-1]]

    # 마지막 버스에 빈자리 있으면 거기 타자
    if len(last_bus) < m:
        return int2hhmm(bus_times[-1])

    # 마지막 버스에 탑승한 제일 늦게 온 사람보다 1분 빨리 와서 뺏어 타자
    return int2hhmm(max(last_bus) - 1)
