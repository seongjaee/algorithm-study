def convert(number, k):
    result = ''
    while number > 0:
        q, r = divmod(number, k)
        number = q
        result += str(r)
    return result[::-1]

def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False

    return True


def solution(n, k):
    answer = 0
    converted_num = convert(n, k)
    for num in converted_num.split('0'):
        if num and is_prime(int(num)):
            answer += 1

    return answer

print(solution(11010101, 10))