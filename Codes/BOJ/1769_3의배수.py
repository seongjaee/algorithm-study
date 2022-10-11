import sys

input = sys.stdin.readline


X = list(map(int, list(input().rstrip())))
cnt = 0
while len(X) > 1:
    s = sum(X)
    X = list(map(int, str(s)))
    cnt += 1

print(cnt)
print("YES" if X[0] % 3 == 0 else "NO")
