import sys
input = sys.stdin.readline

# 모든 심사대가 k까지 끝나는 게 가능한가요?
def check(k):
    result = 0
    for t in times:
        result += k // t
    return result >= m

n, m = map(int, input().split())
times = [int(input()) for _ in range(n)]
times.sort()

left, right = 0, times[-1] * m + 1

while left + 1 < right:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid
    
print(right)


