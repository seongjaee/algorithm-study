e, s, m = map(int, input().split())
now = s

e %= 15
s %= 28
m %= 19

while True:
    if now % 15 == e and now % 19 == m:
        print(now)
        break
    else:
        now += 28