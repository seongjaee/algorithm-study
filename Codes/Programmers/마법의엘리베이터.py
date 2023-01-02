def solution(storey):
    # now: 현재 들고 있는 숫자
    # level: 현재 0으로 만들고자 하는 인덱스 번호 뒤에서부터
    # cnt: 현재까지 이동 횟수
    def backtrack(now, level, cnt):
        nonlocal answer
        if now == 0:
            answer = min(answer, cnt)
            return

        if cnt >= answer:
            return

        k = len(str(now))
        target_index = k - 1 - level
        target_num = int(str(now)[target_index])
        digit = level

        backtrack(
            now + (10 - target_num) * (10**digit), level + 1, cnt + 10 - target_num
        )
        backtrack(now - target_num * (10**digit), level + 1, cnt + target_num)

    answer = 100
    backtrack(storey, 0, 0)

    return answer
