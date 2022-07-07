s = input()

left, right = 0, len(s) - 1
cnt = 0

while left < right:
    if s[left] != s[right]:  # 전체가 회문이 아님
        print(len(s))
        break
    left += 1
    right -= 1

else:
    # 전체가 회문인 경우
    for i in range(1, len(s)):
        if s[i] != s[0]:
            print(len(s) - 1)
            break
    else:
        print(-1)
