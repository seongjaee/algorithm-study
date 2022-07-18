s = input()
cnt = [0] * 26
for char in s:
    cnt[ord(char) - 97] += 1
print(*cnt)
