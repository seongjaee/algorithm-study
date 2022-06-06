import math
a, b = map(int, input().split())

# 2^k까지 1의 개수 합
def sum_to_squarek(k):
    return int(k * (2 ** (k - 1)) + 1)

# 1 ~ x까지의 1의 개수 합
def sum_x(x):
    if x <= 1 :
        return 0
    logx_jin = math.floor(math.log2(x))
    result = sum_to_squarek(logx_jin)
    result += int(sum_x(x - 2 ** logx_jin) + x - 2 ** logx_jin)
    return result

print(sum_x(b) - sum_x(a - 1))