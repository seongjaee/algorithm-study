from collections import deque

n = int(input())
numbers = deque([*map(int, input().split())])

# 누가 뒤집힌 애들인가
# 뒤집히지 않았다면 오른쪽 숫자와의 차이가 1이거나 -(n-1)이다.
revs = deque([0] * n)
for i in range(n - 1):
    if (numbers[i + 1] - numbers[i] + n) % n == 1:
        revs[i] = 1
        revs[i + 1] = 1

if (numbers[0] - numbers[-1] + n) % n == 1:
    revs[0] = 1
    revs[-1] = 1

cnt = sum(revs)  # 뒤집히지 않은 개수

# 뒤집히지 않은 게 전부 맨 앞으로 올 때까지 오른쪽 밀기
right = 0  # 입력값 중 오른쪽에 있던 뒤집히지 않은 수 개수
while right < n:
    total = 0
    for i in range(cnt):
        total += revs[i]
    if total == cnt:
        break
    numbers.appendleft(numbers.pop())
    revs.appendleft(revs.pop())
    right += 1

curr_index_of_1 = numbers.index(1)

if cnt == 0:  # 전부 뒤집힘
    if curr_index_of_1 == 0:
        # print("Case 1")
        print(2)
        print(1, n)
        print(1)
    else:
        # print("Case 2")
        print(numbers[0] - 1)  # 현재 맨앞에 있는 숫자가 맨 앞으로 올때 까지 왼쪽 밀기
        print(1, n)
        print(n - 1)

else:
    if right == 0:
        if curr_index_of_1 == 0:
            # print("Case 3")
            print(1)  # 1이 맨 뒤로 가도록 왼쪽 밀기
            print(cnt, n - 1)  # 뒤에서 1 건너뛰고 뒤집기
            print(n - 1)  # 다시 1이 맨앞으로 가도록 왼쪽 밀기
        else:
            # print("Case 4")
            print(numbers[0])  # 현재 맨 앞에 있는 숫자가 맨 뒤로 갈때까지 왼쪽 밀기
            print(cnt, n - 1)  # 뒤에서 1개 건너뛰고 뒤집기
            print(n - 1)  # 다시 numbers[0]이 맨 앞에 오도록 왼쪽 밀기
    else:
        if curr_index_of_1 == 0:
            # print("Case 5")
            print(1)  # 1이 맨 뒤로 가도록 왼쪽 밀기
            print(cnt, n - 1)  # 뒤에서 1 건너뛰고 뒤집기
            print(right - 1)  # right번 오른쪽으로 밀면 1이 맨앞으로 가도록 왼쪽 밀기
        else:
            # print("Case 6")
            print(numbers[0] - 1)  # 현재 맨 앞에 있는 숫자가 맨 앞에 올때까지 왼쪽 밀기.
            print(cnt + 1, n)  # 뒤집기
            print(right)  # 다시 right번 왼쪽 밀기
