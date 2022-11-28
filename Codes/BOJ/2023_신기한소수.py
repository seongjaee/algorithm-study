import sys

input = sys.stdin.readline


def is_prime(num):
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


N = int(input())
primes = [2, 3, 5, 7]
for _ in range(N - 1):
    next_primes = []
    for p in primes:
        i = 1
        while i < 10:
            next_p = p * 10 + i
            if is_prime(next_p):
                next_primes.append(next_p)
            if next_p % 6 == 1 or i == 3:
                i += 4
            else:
                i += 2

    primes = next_primes

for p in primes:
    print(p)


# 두번째 풀이
def is_prime(k):
    if k in primes:
        return True
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0:
            return False

    primes.add(k)
    return True


def solution(level, now):
    if level == n:
        print(now)
        return

    for i in ["1", "3", "7", "9"]:
        nxt = now + i
        if is_prime(int(nxt)):
            solution(level + 1, nxt)


primes = {2, 3, 5, 7}
n = int(input())

solution(1, "2")
solution(1, "3")
solution(1, "5")
solution(1, "7")
