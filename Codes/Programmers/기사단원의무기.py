def solution(number, limit, power):
    def count_divisor(number):
        result = 0
        for i in range(1, int(number**0.5) + 1):
            if number % i == 0:
                result += 2
                if i == number // i:
                    result -= 1

        return result

    answer = 0
    for i in range(1, number + 1):
        cnt_div = count_divisor(i)
        if cnt_div > limit:
            answer += power
        else:
            answer += cnt_div

    return answer
