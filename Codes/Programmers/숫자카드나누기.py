from functools import reduce
from math import gcd


def is_coprime(numbers, x):
    for num in numbers:
        if num % x == 0:
            return False
    return True


def common_divisor(array):
    return reduce(lambda x, y: gcd(x, y), array, array[0])


def solution(arrayA, arrayB):
    answer = 1
    gcdA = common_divisor(arrayA)
    gcdB = common_divisor(arrayB)

    for i in range(gcdA, 1, -1):
        if gcdA % i == 0 and is_coprime(arrayB, i):
            answer = i
            break

    for j in range(gcdB, answer, -1):
        if gcdB % j == 0 and is_coprime(arrayA, j):
            answer = j
            break

    return answer if answer != 1 else 0
