N = input()
number = list(map(int, N))
k = len(number)

result = [0] * 10

num = number[0]
for j in range(1, 10):
    if j > num:
        pass
    elif j == num:
        B = int(N[1:]) if k > 1 else 0
        result[j] += B + 1
    else:
        result[j] += 10 ** (k - 1)

for i in range(1, k):  # i번째 자리
    num = number[i]
    A = int(N[:i])
    B = int(N[i + 1 :]) if i < k - 1 else 0
    for j in range(10):  # j가 등장한 횟수 구하기
        if j > num:
            result[j] += 10 ** (k - 1 - i) * A
        elif j == num:
            if j == 0:
                result[j] += 10 ** (k - 1 - i) * (A - 1) + (B + 1)
            else:
                result[j] += 10 ** (k - 1 - i) * A + (B + 1)
        else:
            if j == 0:
                result[j] += 10 ** (k - 1 - i) * A
            else:
                result[j] += 10 ** (k - 1 - i) * (A + 1)

print(*result)
