s = input()
cnt = 0
for idx, char in enumerate(s[:-1]):
    if char != s[idx + 1]:
        cnt += 1

print((cnt + 1) // 2)
