def solution(s):
    n = len(s)
    answer = n
    # 단위 문자열 길이별로 확인
    for unit_length in range(1, (n // 2) + 1):
        prev = ""
        cnt = 0
        compressed = ""

        # 앞에서부터 자르기
        for i in range(0, n, unit_length):
            now = s[i : i + unit_length]
            if prev == now:
                cnt += 1
            else:
                if cnt > 1:
                    compressed += str(cnt) + prev
                else:
                    compressed += prev
                prev = now
                cnt = 1

        # 남은 문자열
        if cnt > 1:
            compressed += str(cnt) + prev
        else:
            compressed += prev

        answer = min(answer, len(compressed))

    return answer
