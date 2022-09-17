import sys

input = sys.stdin.readline


def next_permutation(word):
    for i in range(len(word) - 1, 0, -1):
        if word[i - 1] < word[i]:
            for j in range(len(word) - 1, 0, -1):
                if word[i - 1] < word[j]:
                    word[i - 1], word[j] = word[j], word[i - 1]
                    word = word[:i] + sorted(word[i:])
                    return word
    return False


n = int(input())
for _ in range(n):
    word = sorted(input().rstrip())
    while word:
        print("".join(word))
        word = next_permutation(word)
