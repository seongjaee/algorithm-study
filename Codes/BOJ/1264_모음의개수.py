vowels = {"a", "e", "i", "o", "u"}

while True:
    sentence = input().rstrip()
    if sentence == "#":
        break
    cnt = 0
    for char in sentence.lower():
        if char in vowels:
            cnt += 1
    print(cnt)
