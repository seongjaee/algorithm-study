import sys
input = sys.stdin.readline


def brute(arr, now, level, k):
    if level == len(arr):
        if k:
            right[now] = right.get(now, 0) + 1
        else:
            left[now] = left.get(now, 0) + 1
        return
    
    now += arr[level]
    brute(arr, now, level + 1, k)
    now -= arr[level]
    brute(arr, now, level + 1, k)
    

n, s = map(int, input().split())
numbers = [*map(int, input().split())]
numbers.sort()

# key가 나온 횟수 : value
left = {}
right = {}

brute(numbers[:n//2], 0, 0, 0)
brute(numbers[n//2:], 0, 0, 1)

left_key = sorted(left.keys())
right_key = sorted(right.keys(), reverse=True)

li = 0
ri = 0

answer = 0
while li < len(left) and ri < len(right):
    now = left_key[li] + right_key[ri]
    if now > s:
        ri += 1
    elif now == s:
        # 같은게 나왔으면 개수 * 개수만큼 카운트
        answer += left[left_key[li]] * right[right_key[ri]]
        ri += 1
    else:
        li += 1

# 둘다 공집합인 경우 제외
if s == 0:
    answer -= 1

print(answer)
