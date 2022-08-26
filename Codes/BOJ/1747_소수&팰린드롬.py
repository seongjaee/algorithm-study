import sys

input = sys.stdin.readline


def is_palindrome(number):
    s = str(number)
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


is_prime = [True] * 2000000
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(2000000**0.5) + 1):
    if is_prime[i]:
        for j in range(i + i, 2000000, i):
            is_prime[j] = False


n = int(input())
for i in range(n, 2000000):
    if is_prime[i] and is_palindrome(i):
        print(i)
        break
