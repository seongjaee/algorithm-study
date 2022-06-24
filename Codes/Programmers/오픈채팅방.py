def solution(record):
    uid_nickname = {}
    result = []
    for msg in record:
        info = msg.split(" ")
        if info[0] == "Enter":
            result.append((info[1], "님이 들어왔습니다."))
            uid_nickname[info[1]] = info[2]
        elif info[0] == "Leave":
            result.append((info[1], "님이 나갔습니다."))
        elif info[0] == "Change":
            uid_nickname[info[1]] = info[2]

    return [uid_nickname[x[0]] + x[1] for x in result]
