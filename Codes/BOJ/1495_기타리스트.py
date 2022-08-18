n, s, m = map(int, input().split())
numbers = [*map(int, input().split())]

arr = {s}
for num in numbers:
    temp = set()
    for x in arr:
        for nxt in [x + num, x - num]:
            if 0 <= nxt <= m:
                temp.add(nxt)
    arr = temp

if arr:
    print(max(arr))
else:
    print(-1)
