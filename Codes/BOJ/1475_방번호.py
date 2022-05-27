n = input()

counter = {}
for char in n:
    counter[char] = counter.get(char, 0) + 1

max_cnt = 0
max_key = []

cnt6 = counter.get('6', 0)
cnt9 = counter.get('9', 0)

total = cnt6 + cnt9

counter['6'] = total // 2 + total % 2
counter['9'] = total // 2 + total % 2

for key, cnt in counter.items():
    if cnt > max_cnt:
        max_cnt = cnt
        max_key = [key]
    elif cnt == max_cnt:
        max_key.append(key)
    
print(max_cnt)
